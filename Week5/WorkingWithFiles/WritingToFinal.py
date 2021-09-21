def write_to_file(file, order_item):
    try:
        with open(file, "a") as file:
            file.write(order_item+"\n")
    except FileNotFoundError:
        print("The file "+file+" does not exist") #While there is the "w" in open, this error won't show as "w" creates the file


write_to_file("writing_test.txt", "Banana")