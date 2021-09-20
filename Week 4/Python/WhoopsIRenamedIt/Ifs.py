print("How old are you?")
age = int(input())

if age >= 100:
    print("Congrats on making it to that age, but is the cinema the best place\nfor you?")
elif age >= 18:
    print("No limitations on the films you can see")
elif age >= 12:
    print("Go for it, but don't blame us if you're traumatised")
else:
    print("Peppa pig is calling")