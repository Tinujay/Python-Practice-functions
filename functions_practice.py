#A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello():
    print('Hello user!')

hello()

#A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(x , y, z):
    return [x, y, z]

result = pack('apple', "cherry", "grape")
print(result)


#A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.
def eat_lunch(list_items):
    if not list_items:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {list_items[0]}")
        for item in list_items[1:]:
            print(f"Next I eat {item}")

eat_lunch([]) #My lunchbox is empty!
eat_lunch(["eggs", "toast", "oatmeal"])