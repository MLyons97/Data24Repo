import math                                     #Math package needed for square root
FactoringNumber = 600851475143                  #Declaring attributes
i = 2
ResultsHolder = []

while i < math.sqrt(FactoringNumber):           #Looping up to the square root means no factors will be repeated
    if FactoringNumber % i == 0:                #If the number is divisible, we do things, if not we move
        FactoringNumber = FactoringNumber/i     #We divide it
        ResultsHolder.append(i)                 #And collect the divisor
        i = 2                                   #Reset the "i" counter
    i = i+1                                     #And increment it for every time it isn't divisible
ResultsHolder.append(int(FactoringNumber))      #This will store the final prime number

print(max(ResultsHolder))                       #Max to get the largest
