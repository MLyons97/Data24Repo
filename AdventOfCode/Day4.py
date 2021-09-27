import pprint

req_cats = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def check_cats(string_to_check, reference_string):
    if string_to_check in reference_string:
        return True
    else:
        return False

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
#print(clear_passports[0])

one_line_passports = []
for i in clear_passports:
    for j in i:
        if i not in one_line_passports:
            one_line_passports.append(i)

pprint.pprint(one_line_passports[0:5])

successful_passports = 0

for i in range(0, 5, 1):
    for j in req_cats:
        reqs = 0
        print(str(one_line_passports[i]))
        for k in one_line_passports[i]:
            print(j)
            print(k)
            print(j in k)
            if j in k:
                reqs += 1
    print(f"reqs = {reqs}")
    if reqs == 7:
        successful_passports += 1



# for x in range(0, 5, 1):
#     print(x)
#     category_passed = 0
#     for i in req_cats:
#         for j in clear_passports[x]:
# #            print(f"i = {i}, j = {j}")
#             if i in j:
#                 category_passed += 1
#
#     if category_passed == 8:
#         print(f"{x} was successful")
#         successful_passports += 1

print(successful_passports)


# print(valid_passports)
