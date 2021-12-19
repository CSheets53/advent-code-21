from json import dumps

current_index = 0

def main():
    f = open("../inputs/d16.txt")
    input_hex = [line.rstrip('\n') for line in f][0]
    whole_packet_bin = bin(int(input_hex, 16))[2:].zfill(len(input_hex) * 4)

    main_packet = parse_packet(whole_packet_bin)
    # print(dumps(main_packet, sort_keys=False, indent=4))
    print(f"Part 1: {part1(main_packet)}")
    print(f"Part 2: {part2(main_packet)}")

def parse_packet(packet_bin: str, parent=None):
    global current_index

    new_packet = {
        "version": int(packet_bin[current_index:current_index+3], 2),
        "type_id": int(packet_bin[current_index+3:current_index+6], 2),
        "bit_len": 0,
        "value": None
    }

    current_index += 6
    new_packet["bit_len"] += 6
    if new_packet["type_id"] == 4:
        # Literal
        segments = []
        while True:
            new_segment = packet_bin[current_index:current_index+5]
            current_index += 5
            segments.append(new_segment[1:])

            if new_segment[0] == '0':
                break

        bit_str = ''.join(segments)
        new_packet["value"] = int(bit_str, 2)
        new_packet["bit_len"] += (len(bit_str) + len(segments))
    else:
        #Operator
        new_packet["length_type_id"] = packet_bin[current_index]
        current_index += 1
        new_packet["bit_len"] += 1

        if new_packet["length_type_id"] == '0':
            # Use sub_bit_len to count the number of bits parsed for sub-packets
            new_packet["sub_bit_len"] = int(packet_bin[current_index:current_index+15], 2)
            current_index += 15
            new_packet["bit_len"] += 15
        else:
            new_packet["num_sub"] = int(packet_bin[current_index:current_index+11], 2)
            current_index += 11
            new_packet["bit_len"] += 11
        
        new_packet["sub"] = []
        parse_packet(packet_bin, new_packet)

        # Type ID rules (Part 2)
        if new_packet["type_id"] == 0:
            packet_sum = 0
            for packet in new_packet["sub"]:
                packet_sum += packet["value"]
            new_packet["value"] = packet_sum

        elif new_packet["type_id"] == 1:
            packet_prod = 1
            for packet in new_packet["sub"]:
                packet_prod *= packet["value"]
            new_packet["value"] = packet_prod

        elif new_packet["type_id"] == 2:
            min_packet_val = new_packet["sub"][0]["value"]
            for packet in new_packet["sub"]:
                if packet["value"] < min_packet_val:
                    min_packet_val = packet["value"]
            new_packet["value"] = min_packet_val

        elif new_packet["type_id"] == 3:
            max_packet_val = new_packet["sub"][0]["value"]
            for packet in new_packet["sub"]:
                if packet["value"] > max_packet_val:
                    max_packet_val = packet["value"]
            new_packet["value"] = max_packet_val

        elif new_packet["type_id"] == 5:
            if new_packet["sub"][0]["value"] > new_packet["sub"][1]["value"]:
                new_packet["value"] = 1
            else:
                new_packet["value"] = 0

        elif new_packet["type_id"] == 6:
            if new_packet["sub"][0]["value"] < new_packet["sub"][1]["value"]:
                new_packet["value"] = 1
            else:
                new_packet["value"] = 0

        elif new_packet["type_id"] == 7:
            if new_packet["sub"][0]["value"] == new_packet["sub"][1]["value"]:
                new_packet["value"] = 1
            else:
                new_packet["value"] = 0

    if parent:
        parent["sub"].append(new_packet)
        parent["bit_len"] += new_packet["bit_len"]

        if parent["length_type_id"] == '0':
            parent["sub_bit_len"] -= new_packet["bit_len"]

            if parent["sub_bit_len"] > 0:
                parse_packet(packet_bin, parent)
        else:
            if len(parent["sub"]) != parent["num_sub"]:
                parse_packet(packet_bin, parent)
    else:
        return new_packet

def part1(main_packet):
    version_nums = []

    def _recurse_packet_versions(current_packet):
        version_nums.append(current_packet["version"])

        if current_packet.get("sub"):
            for sub in current_packet["sub"]:
                _recurse_packet_versions(sub)

    _recurse_packet_versions(main_packet)

    return sum(version_nums)

def part2(main_packet):
    return main_packet["value"]

if __name__ == "__main__":
    main()
