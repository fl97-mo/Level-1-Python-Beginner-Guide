# collection = "variable" used to store multiple values.                                                                                       |
# Lists[] = defined with [], list1[item1,item2,...]                                                                                            |
# - ordered: items remain in their order as inserted                                                                                           |
# - changeable: add, remove or modify items.                                                                                                   |
# - allows duplicates: same value can appear multiple times                                                                                    |
# - a bit slower, but most flexible                                                                                                            |
# Set{}   = definded with {}. set1{item1,item2,...}                                                                                            |
# - unordered: items have no fixed positions, postion can change                                                                               |
# - No duplicates: each value must be unique                                                                                                   |
# - Add/Remove items: you can add or remove items, but not edit existing items                                                                 |
# - faster than lists                                                                                                                          |
# Tuple() = defined with (). tuple1(item1,item2,...)                                                                                           |
# - ordered = items keep their position, like in a list                                                                                        |
# - immutable = once created, you can't add, remove or edit                                                                                    |
# - allows duplicates: same value can appear multiple times                                                                                    |
# - faster, but less flexible                                                                                                                  |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# Lists:                                                                                                                                       |
shopping_cart = ["Red Apple", "Coca Cola", "Green Apple", "Butter"]    # Define a list of products                                             |
shopping_cart.append("Orange Juice")                                   # Add an item to the end of the list with .append                       |
shopping_cart.insert(1, "Vanilla Milk")                                # Insert an item into a specific postion with .insert(index, newitem)   |
shopping_cart.remove("Coca Cola")                                      # Remove a specific item with .remove                                   |
shopping_cart.pop(0)                                                   # Remove an item by its index .pop(index)                               |
shopping_cart.sort()                                                   # Sort the list in ascending order                                      |
shopping_cart.reverse()                                                # Reverse the order of the list                                         |
nested_list = [["Apple", 3], ["Milk", 2]]                              # A list of lists. [[list1],[list2]]                                    |
print(shopping_cart)                                                   # Display the list                                                      |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#['Vanilla Milk', 'Orange Juice', 'Green Apple', 'Butter']                                                                                     |
#----------------------------------------------------------------------------------------------------------------------------------------------|
print(shopping_cart[0])                                                # print the item on specific index                                      |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#Vanilla Milk                                                                                                                                  |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# Lists are ideal for using dynamic and ordered data. Example: shopping list, you can remove, add, change items                                |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# Sets:                                                                                                                                        |
unique_items = {"Apple", "Cola", "Butter","Magazine", "Cherries"}      # Define a set of unique items                                          |
unique_items.discard("Cola")                                           # Remove an item with .discard(item) (no error if item not found)       |
unique_items.update(["Juice", "Apple"])                                # Add multiple items to the set .update([item1,item2])                  |
unique_items.remove("Apple")                                           # Remove an item with .remove(item) (error if item not found)           |
unique_items.clear()                                                   # Remove all items from the set with .clear()                           |
unique_items.add("Milk")                                               # Add an item to the set with .add(item)                                |
print(unique_items)                                                    # Display the set                                                       |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#{'Milk'}                                                                                                                                      |
# Sets are useful for storing unique items, e.g., product types in the supermarket                                                             |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# Tuples:                                                                                                                                      |
payment_methods = ("Cash", "Credit Card", "Mobile Payment")             # Define a tuple for available payment methods.                        |
print(len(payment_methods))                                             # Get the number of items in the tuple.                                |
print(payment_methods)                                                  # Display the tuple                                                    |
# --Terminal Output----------------------------------------------------------------------------------------------------------------------------|
# 3                                                                                                                                            |
# ('Cash', 'Credit Card', 'Mobile Payment')                                                                                                    |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# Tuples are great for storing fixed data that does not need to be modified, e.g., payment options in a supermarket                            |
#----------------------------------------------------------------------------------------------------------------------------------------------|


