from sys import maxsize

def main():
    f = open("../inputs/d17.txt")
    target_area_str = [line.rstrip('\n') for line in f][0]
    f.close()

    target_area = target_area_str.split(": ")[1].split(", ")
    x_range_str = target_area[0].split('=')[1].split("..")
    x_min, x_max = int(x_range_str[0]), int(x_range_str[1])

    y_range_str = target_area[1].split('=')[1].split("..")
    y_min, y_max = int(y_range_str[0]), int(y_range_str[1])

    part1, part2 = run(x_min, x_max, y_min, y_max)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

def run(x_min, x_max, y_min, y_max):
    """
    Part 1: Find the highest y position reachable to get the probe in the target area
    Part 2: Find how many distinct initial velocities land the probe in the target area
    """
    highest_y_pos = -maxsize
    distinct_vels = set()

    for x_velocity in range(1, x_max + 1):
        for y_velocity in range(y_min, -y_min + 1):
            highest_test_y_pos = -maxsize
            in_area = False

            current_probe_x = 0
            current_probe_y = 0

            x_vel = x_velocity
            y_vel = y_velocity

            while current_probe_x <= x_max and current_probe_y >= y_min:
                # Run steps to try getting probe in position
                current_probe_x += x_vel
                current_probe_y += y_vel

                if current_probe_y > highest_test_y_pos:
                    highest_test_y_pos = current_probe_y

                if x_vel > 0:
                    x_vel -= 1
                elif x_vel < 0:
                    x_vel += 1

                y_vel -= 1

                if current_probe_x >= x_min and current_probe_x <= x_max and current_probe_y >= y_min and current_probe_y <= y_max:
                    in_area = True
                    break

            if in_area:
                if highest_test_y_pos > highest_y_pos:
                    highest_y_pos = highest_test_y_pos
                distinct_vels.add((x_velocity, y_velocity))

    return highest_y_pos, len(distinct_vels)

if __name__ == "__main__":
    main()
