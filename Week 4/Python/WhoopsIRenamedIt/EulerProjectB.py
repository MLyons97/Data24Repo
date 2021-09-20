A = 1
B = 2
C = FinalSum = 0

while A < 4000000:
    if A % 2 == 0:
        FinalSum = FinalSum + A
    C = A+B
    A = B
    B = C
print(FinalSum)