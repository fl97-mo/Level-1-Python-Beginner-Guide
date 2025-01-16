# there are two basic loop types in python                                                                 |
# - while loop = Execute some code while a condition is true.                                              |
# - for loop = Execute a block of code a fixed number of times.                                            |
# use while loops when you don't know in advance how many iterations are needed                            |
# use for loops when you know the number of iterations                                                     |
#----------------------------------------------------------------------------------------------------------|
# WHILE LOOPS                                                                                              |
#----------------------------------------------------------------------------------------------------------|
# Example 1: Ask if a user is over 18.                                                                     |
age = int(input("Enter your age: "))                  # age input                                          |
while age <18:                                        # do the loop while the age is below 18              |
    print("Please come back when you are over 18.")   # age is still below 18, so this code continues      |
    age = int(input("Enter your age: "))              # ask again for user input, until they're 18+        |
print(f"You are {age} years old!")                    # loop escaped, user is 18+ so, do continue this code|
#----------------------------------------------------------------------------------------------------------|
# Example 2: Breaking out of a loop                                                                        |
while True:                                           # infinite loop, runs until we break it              |
    checkout = int(input("1 = Buy, 2 = Cancel"))      # user input for a menu selection                    |
    if checkout == 1:                                 # if 1, you buy 100 apples                           |
        print("You bought 100 apples.")               # infinite                                           |
    elif checkout == 2:                               # if 2                                               |
        print("Byebye!")                              # print this and                                     |
        break                                         # break condition to escape out of loop              |
    else:                                             # if user input is anything else than 1 or 2         |
        print("Enter 1 to buy, or 2 to cancel.")      # repeat asking for valid user input                 |
#----------------------------------------------------------------------------------------------------------|
# Example 3: Using while to iterate through an list                                                        |
inventory = ["Apples", "Bananas", "Cherries", "Eggs"] # list of all available products                     |
search = input("What product are you looking for? ")  # user input                                         |  
position = 0                                          # start index for list                               |
while position < len(inventory):                      # Loop through (the length of) the inventory         |
    if inventory[position].lower() == search.lower(): # .lower incase user types "eggs" instead of "Eggs"  |
                                                      # if the user input is found in the current position |
                                                      # (or in the list since it iterates through)         |
        print(f"{search} is in stock!")               # print the message                                  |
        break                                         # Exit the loop if found                             |
    position += 1                                     # Increment the index, as long as the length of list |
else:                                                 # If no break occurs, execute this                   |
    print(f"Sorry, {search} is not available.")       #                                                    |
# FOR LOOPS                                                                                                |
#----------------------------------------------------------------------------------------------------------|
# Example 1: List all products in stock.                                                                   |
products = ["Apple", "Cheese", "Milk", "Gunpowder"]   # Define a list of products                          |
for product in products:                              # iterate through the list of products               |
                                                      # product = name of element within list products     |
    print(f"We have {product} in stock.")             # Print each product                                 |
# Example 2: Skip iterations with continue                                                                 |
inventory = ["Raisin cookies","Eggs", "Raisin cakes"] # List of our inventory                              |
print("Display only raisin products")                 # we want to sort out non-raisin products            |
for product in inventory:                             # go through the list of products                    |
    if not product.startswith("Raisin"):              # if a product doesnt start with raisin              |
        continue                                      # skip it                                            |
    print(f"{product}")                               # if it does, print the product                      |
#----------------------------------------------------------------------------------------------------------|
# Example 3: Reverse loop for countdown                                                                    |
for i in reversed(range(1,6)):                        # print i, but in the reversed range from 1-5        |
    print(f"Shift over in {i} seconds.")              # do this "range" amount of times                    |
print("Shift over, time to go home!")                 # after you did the range, continue with code        |
#----------------------------------------------------------------------------------------------------------|
