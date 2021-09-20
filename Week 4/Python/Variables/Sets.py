##Sets can't have repeated values BUT are mutable
##unless you make it as a frozen set (x=frozenset(set,stuff,goes,in,here)
Car_Parts = {"Wheels", "Engine", "Gearbox", "Doors", "Windscreen"}
print(Car_Parts)
Car_Parts.add("Wing mirrors")
print(Car_Parts)

#As they can't have repeated values, can be used to test anagrams
a = "nameless"
b = "salesman"

print((set(a) == set(b)) & (len(a) == len(b)))