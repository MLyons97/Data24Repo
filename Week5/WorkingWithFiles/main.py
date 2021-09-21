
with open('order.txt', 'r') as file:                             # Can do it this way instead of file = open(order.txt)
    file_contents = file.readlines()                        # and then closing it at the end

#    for line in file_contents:
    #    print(line.replace("\n", ""))



with open('order.txt', 'w') as file:

    order_items = ["fries", "onion rings", "drink"]

    for item in order_items:
        file.write(item + "\n")

