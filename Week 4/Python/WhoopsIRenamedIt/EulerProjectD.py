def palcheck(numb):
    back = str(numb)[::-1]
    if str(numb) == back:
        return True
    else:
        return False


highest_val = 0
highest_prods = [0, 0]

for i in range(100, 999, 1):
    for j in range(100, 999, 1):
        if palcheck(i*j) and i*j > highest_val:
            highest_val = i*j
            highest_prods[0] = i
            highest_prods[1] = j
print(highest_val)
print(highest_prods)
