# def add(number1, number2):
#     return number1 + number2
#
#
# addition = lambda num1, num2: num1 + num2 ## does the same as add above
#
# print(addition(3,6))

# Best used with the map function

savings = [234, 555, 674, 78]

bonus = map(lambda x: x*1.1, savings)
            #function        list
# The function is applied to every element of the list
# so the lambda function creates the function to be applied
# to the list that is savings
print(list(bonus))
