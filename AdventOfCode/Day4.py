import pprint

with open("Passports.txt") as passport_file:
    read_file = passport_file.readlines()
    passports = [[] for i in range(len(read_file))]
    left_to_read = True
    k = 0
    for j in range(0, len(read_file)):
        if read_file[j] != "\n":
            passports[k].append(read_file[j].rstrip("\n").strip("\n"))
        else:
            k += 1
            j += 1

clear_passports = [x for x in passports if x != []]
pprint.pprint(clear_passports)
