# Dictionary = collection of {key:value} pair                                                                                                  |
# Key = an identifier, example {"Apple"   ; has to be unique in the dictionary                                                                 |
# Value = data associated with the key. :1.00}(€). could be also True, "Red", etc.  ; can occur multiple times within dictionary               |
# Are ideal for data with a clear relationship, like product and price                                                                         |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# Example 1: Create and print dictionary                                                                                                       |
products = {"Apple":0.75,"Banana":0.95,"Kiwi":1.00, "Egg":0.30}        # Created a dictionary of products = {key1:value1,key2:value2,etc.}     |
print(products)                                                        # Print the dictionary                                                  |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#{'Apple': 0.75, 'Banana': 0.95, 'Kiwi': 1.0, 'Egg': 0.3}                                                                                      |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# Example 2: Look for a specific value of a key                                                                                                |
print(f"The price of an Apple is: {products["Apple"]}€")                # Use the key "Apple" to get its value                                 |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#The price of an Apple is: 0.75€                                                                                                               |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# Example 3: Check if a product exists                                                                                                         |
if "Kiwi" in products:                                                  # Check if "Kiwi" exists as a key in the dictionary product            |
    print("Kiwi is available.")                                         # If yes, print this                                                   |
else:                                                                   # In any other case then yes                                           |
    print("Kiwi is not available.")                                     # Print this                                                           |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#Kiwi is available.                                                                                                                            |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# Example 4: Add, update, and remove items                                                                                                     |
products.update({"Milk": 1.20})                                         # Add a new product to the dictionary                                  |
print(products)                                                         # Print products                                                       |
                                                                        #                                                                      |
products["Banana"] = 1.10                                               # Update the value of a key                                            |
print(products)                                                         # Print products                                                       |
                                                                        #                                                                      |
products.pop("Egg")                                                     # Remove a product by its key using .pop()                             |
print(products)                                                         # Print products                                                       |
                                                                        #                                                                      |
products.clear()                                                        # Remove all items from the dictionary                                 |
print(products)                                                         # Print products                                                       |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#{'Apple': 0.75, 'Banana': 0.95, 'Kiwi': 1.0, 'Egg': 0.3, 'Milk': 1.2}  # After addding milk                                                   |
#{'Apple': 0.75, 'Banana': 1.1, 'Kiwi': 1.0, 'Egg': 0.3, 'Milk': 1.2}   # After updating banana's value                                        |
#{'Apple': 0.75, 'Banana': 1.1, 'Kiwi': 1.0, 'Milk': 1.2}               # After removing egg                                                   |
#{}                                                                     # After removing all items                                             |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# Example 5: Get a list of keys, values, or key-value pairs                                                                                    |
products = {"Apple":0.75,"Banana":0.95,"Kiwi":1.00, "Egg":0.30}         # Readding keys, values since we cleared all earlier                   |
print(products.keys())                                                  # Print all keys                                                       |
                                                                        #                                                                      |
print(products.values())                                                # Print all values                                                     |
                                                                        #                                                                      |
print(products.items())                                                 # Print all key-value pairs as tuples                                  |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#dict_keys(['Apple', 'Banana', 'Kiwi', 'Egg'])                          # All keys in products                                                 |
#dict_values([0.75, 0.95, 1.0, 0.3])                                    # All values in products                                               |
#dict_items([('Apple', 0.75), ('Banana', 0.95), ('Kiwi', 1.0), ('Egg', 0.3)]) # All key-value paris as tuples                                  |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# Task 1: Managing a supermarket inventory with dictionaries                                                                                   |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# Defining a dictionary of our inventory                                                                                                       |
products = {"Apple":0.75,"Banana":0.95,"Kiwi":1.00, "Egg":0.30}         # Dictionary = {key1:value1,key2:value2}                               |
# Looping through the dictionary to display all products                                                                                       |
print("Our products and their prices: ")                                                                                                      #|
for product, price in products.items():                                 # For key, value in dictionary.items():                                |
    print(f"{product}: {price}")                                        # F-String, print our products and prices                              |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#Our products and their prices:                                                                                                                |
#Apple: 0.75                                                                                                                                   |
#Banana: 0.95                                                                                                                                  |
#Kiwi: 1.0                                                                                                                                     |
#Egg: 0.3                                                                                                                                      |
#----------------------------------------------------------------------------------------------------------------------------------------------|
