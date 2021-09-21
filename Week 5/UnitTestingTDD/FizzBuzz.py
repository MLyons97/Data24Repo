def div_check(numb1, numb2):
    if numb1 % numb2 == 0:
        return True
    else:
        return False


def number_check(i, string):
    if div_check(i, 3): string += "Fizz"
    if div_check(i, 5): string += "Buzz"
    if string == "": string += str(i)
    return string


print_string = ""

for i in range(1, 101, 1):
    print_string = number_check(i, print_string)

    print(print_string)
    print_string = ""
