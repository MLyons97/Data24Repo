
try:
    list1 = [1,2,3,4]
    print(list1[5])
    with open("document.txt") as file:
        data = file.readlines()

except FileNotFoundError as errmsg:
    print("You have deleted the document you fool\n", errmsg)
    raise

except IndexError as errmsg:
    print("List ain't that long\n", errmsg)
    raise                                                           # raise is a keyword that will throw the error again
                                                                    # IE it catches it and throws it onwards (stopping code)

finally:                                                                    # Need to have a try/except for this to work though
    print("This bit will always happen, even if there is an error raised")
