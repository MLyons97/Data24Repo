# # # # # # # # # # # # # # # # Part One # # # # # # # # # # # # # # # #

with open("Map.txt") as map_file:
    read_map = map_file.readlines()

    start_point = [0][0]

    tree_count = 0
    x = 0

    for row in read_map:
        print(row.replace("\n", ""))
    for y in range(len(read_map)):
        if read_map[y][x] == "#":
            tree_count += 1
        if x + 3 <= len(read_map[y])-2:
            x += 3
        else:
            x = len(read_map[y]) - x - (2*(30-x))

    print(f"tree count = {tree_count}")
