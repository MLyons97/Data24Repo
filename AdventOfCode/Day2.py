def get_key_index1(string):
    return int(string.index(":"))


def get_key_index2(string):
    return int(string.index("-"))


def get_key_letter(string: str):
    key_index = get_key_index1(string)
    return string[key_index - 1]


def upper_limit(string: str):
    key_index = get_key_index2(string)
    return int(string[key_index+1: key_index+3])


def lower_limit(string: str):
    key_index = get_key_index2(string)
    if key_index == 1:
        min_count = int(string[key_index-1])
    elif key_index == 2:
        min_count = int(string[key_index-2: key_index])
    else:
        min_count = 1
        print("THIS IS A HUGE ERROR RIGHT HERE IN THE LOWER LIMIT FUNCTION")
    return min_count


def part_one_stuff(string:str):

    def count_the_substring(letter, string):
        mid_index = get_key_index1(string)
        return string.count(letter, mid_index)

    letter = get_key_letter(string)
    count = count_the_substring(letter, string)

    max = upper_limit(string)
    min = lower_limit(string)

    if min <= count <= max:
        return True
    else:
        return False


def part_two_stuff(string:str):
    key_letter = get_key_letter(data[i])
    key_req1 = lower_limit(data[i])
    key_req2 = upper_limit(data[i])
    substring = data[i][get_key_index1(data[i]) + 2:]
    substring.strip()
    if (key_letter == substring[key_req1 - 1] and key_letter != substring[key_req2 - 1]) \
    or (key_letter == substring[key_req2 - 1] and key_letter != substring[key_req1 - 1]):
        return True
    else:
        return False


with open('Password_Databast.txt', 'r') as passwords:
    data = passwords.readlines()
    correct_counter_part_1: int = 0
    correct_counter_part_2: int = 0
    for i in range(len(data)):
        if part_one_stuff(data[i]):
            correct_counter_part_1 += 1
        if part_two_stuff(data[i]):
            correct_counter_part_2 += 1

    print(correct_counter_part_1)
    print(correct_counter_part_2)




# test_string = "6-9 h: hhthplhgmpzsmhhxhh"
# test_key_letter = get_key_letter(test_string)
# test_key_req = lower_limit(test_string)
# test_key_void = upper_limit(test_string)
# test_substring = test_string[get_key_index1(test_string)+2:]
# print(f"{test_substring[test_key_req]}, {test_substring[test_key_void]}")
#
# if test_key_letter == test_substring[test_key_req] and test_key_letter != test_substring[test_key_void]:
#     print("Yes")
#     correct_counter_part_2 += 1
