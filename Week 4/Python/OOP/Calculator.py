import math


def add(*multiargs) -> float:
    total = 0
    for arg in multiargs:
        total += arg
    return total


def subtract(*multiargs) ->float:
    total = multiargs[0]
    for arg in range(1, len(multiargs), 1):
        total -= multiargs[arg]
    return total


def multiply(*multiargs) ->float:
    total =1
    for arg in multiargs:
        total *= arg
    return total


def divide(*multiargs) -> float:
    total = multiargs[0]
    for arg in range(1, len(multiargs),1):
        total = total/multiargs[arg]
    return total


def root(numb: float) -> float:
    return math.sqrt(numb)


def power(numb: float, pwr: float) -> float:
    return numb ** pwr


print(root(2))