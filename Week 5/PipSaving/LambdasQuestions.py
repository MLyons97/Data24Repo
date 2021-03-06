print("\nQ1a\n")
# Q1a: Replicate the following functions as lambda
# A1a: answers shown below functions



def square(n):
    return n*n


lsquare = lambda n: n*n


def percentage(n):
    return n/100


lper = lambda n: n/100


def multiplier(n, m):
    return n*m


lmult = lambda n, m: n*m


def addition(a, b, c):
    return a + b + c


ladd = lambda a, b, c: a + b + c


print("\nQ1b\n")
# Q1b: Write an explanation of how this factorial lambda function works
factorial = lambda a: a*factorial(a-1) if (a>1) else 1


# A1b:
print("This is a recursive function (it calls itself) and will return the product\
        of all previous numbers (unless a is not factorial-able, in which case\
        it will return one).")


print("\nQ1c\n")
# Q1c: Using the Map function alongside a lambda function, take the list_of_numbers
# and generate a list of all of the numbers squared
list_of_numbers = [23, 345, 45, 76, 87, 4, 2, 0]


# A1c:
list_squared = list(map(lambda x: x*x, list_of_numbers))
print(list_squared)
# -------------------------------------------------------------------------------------- #
