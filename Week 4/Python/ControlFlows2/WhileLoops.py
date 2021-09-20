# age = "a"
#
# while age.isnumeric() == False:
#     age = input("Please input your age")
#
# print(f"Thank you, you are {age} years old")
#
# ##OR more universally done as:

checker = True

while checker:
    age = input("Please input your age: ")
    if age.isdigit() and int(age) < 117:
        checker = False
    else:
        print("Please use numbers, and be realistic, you are not older than the oldest living person")
