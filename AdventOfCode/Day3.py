# # # # # # # # # # # # # # # Global Functions # # # # # # # # # # # # # #
#
#
# def get_position_in_x(string)
#
#
# routes_to_check = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
# # # # # # # # # # # # # # # # # Part One # # # # # # # # # # # # # # # #
#
#
# def part_one():
#     with open("Map.txt") as map_file:
#         read_map = map_file.readlines()
#         tree_count = 0
#         x = 0
#
#         for row in read_map:
#             print(row.replace("\n", ""))
#         for y in range(len(read_map)):
#             #print(y)
#
#             if read_map[y][x] == "#":
#                 tree_count += 1
#             if x + 3 <= len(read_map[y])-2:
#                 x += 3
#             else:
#                 x = loop_round(x, len(read_map[y]))
#
#         print(f"tree count = {tree_count}")
#         # # # # # # # # # # # # # # # # Part Two # # # # # # # # # # # # # # # #
#
#
# def part_two(x_jump, y_jump):
#     tree_count = 0
#     total_product = 1
#     with open("Map.txt") as map_file:
#         read_map = map_file.readlines()
#
#         for y in range(0, len(read_map), y_jump):
#             max_x = len(read_map[y])-2
#             if read_map[y][x] == "#":
#                 tree_count += x_jump
#             if x + x_jump <= len(read_map[y])-2:
#                 x += x_jump
#             else:
#                 x = loop_round(x, len(read_map[y]))
#
#         print(f"tree count = {tree_count}")
#
#
#
#         # tree_count = 0
#         # x = 0


#https://adventofcode.com/2020/day/3

file_path = "Map.txt"      # For you it might be "Day3" or something similar

slopes = [
    {"Right": 1, "Down": 1}
    , {"Right": 3, "Down": 1}
    , {"Right": 5, "Down": 1}
    , {"Right": 7, "Down": 1}
    , {"Right": 1, "Down": 2}
]

# Add extra properties to dictionary
for slope in slopes:
    slope["x"] = slope["trees"] = slope["open"] = 0


with open(file_path, "r") as map:
    map_as_list = list(map)                                 # easier to work with lists
    line_length = len(map_as_list[0].rstrip('\n'))          # used when trying to index out of line length e.g. Line[33]
    line_count = 0                                          # The current line reading from

    for line in map_as_list[1:]:                            # Ignore the first line (line 0)
        line_count += 1

        for slope in slopes:
            # Check if slope skips line
            if line_count % slope["Down"] != 0:
                continue

            # Otherwise traverse line
            line = line.rstrip('\n')
            slope["x"] = (slope["x"] + slope["Right"]) % line_length

            if line[slope["x"]] == '#':
                slope["trees"] += 1
            else:
                slope["open"] += 1


product = 1
for slope in slopes:
    print(f"Trees: {slope['trees']}; Empties: {slope['open']}")
    product *= slope['trees']

print(f"Product = {product}")