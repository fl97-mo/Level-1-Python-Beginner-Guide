# Variables = Storage for Values. Use variables througout your code, for easier use.                                                           |
# You can assign different types of data to a variable                                                                                         |
# choose descriptive names for your variables, to make your code easier to understand                                                          |
# example 1: assigning values to variables                                                                                                     |  
product = "Apple"                                               # String(text): assigned with = "" or = ''                                     |
amount = 90                                                     # Integer(whole number): assign by declaring without decimals                  |
price = 0.55                                                    # Float (decimal number): assign with decimals                                 |
is_fruit = True                                                 # Boolean: only True or False expressions                                      |
abcdef = 40                                                     # abcdef is not a good variable name for a 40% discount                        |
discount_percentage = 40                                        # now we know what you meant by that                                           |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# variables can be reassigned throughout the code, changing values and types                                                                   |                                                                                                                                      
# example 2: reassigning variables                                                                                                             |     
print("I ate an apple")                                         # amount was declared above in example 1 with 90                               |
amount = amount - 1                                             # reassign: we subtract 1 from the amount, because someone got hungry          |
print("Apples left:",amount)                                    # print the new value of amount                                                |
print("My girlfriend is very hungry")                           # let's try different methods to write this                                    |
amount -= 86                                                    # reassign: Operators: -= shortcut for = amount - 86                           |
print(f"Now I only have {amount} apples.")                      # use f-string (f"") to display variables {in_brackets} flexibly               |
print("A raccoon stole my remaining apples.")                   # you can reassign completely different values to a variable                   |
amount = "none left"                                            # instead of an Integer we now assign a String                                 |
print(f"Now I have {amount}.")                                  # new value displayed using f-Strings                                          |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#I ate an apple                                                                                                                                |
#Apples left: 89                                                                                                                               |
#My girlfriend is very hungry                                                                                                                  |
#Now I only have 3 apples.                                                                                                                     |
#A racoon stole my remaining apples.                                                                                                           |
#Now I have none left.                                                                                                                         |
#----------------------------------------------------------------------------------------------------------------------------------------------|
#                                                                                                                                              |                                                                                                                                      
# example 3: assigning multiple variables in one line                                                                                          |     
                                                               # using one line, separating the variables by comma                             |
x,y,z = 1,3,5                                                  # assign 1, 3 and 5 in order to x y z                                           |
print(f"x: {x}\ny: {y}\nz: {z}")                               # printing. use \n within f-Strings to create a line break                      |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#x: 1                                                                                                                                          |
#y: 3                                                                                                                                          |
#z: 5                                                                                                                                          |
#----------------------------------------------------------------------------------------------------------------------------------------------|
# check type of a variable by using type(variable)                                                                                             |
# example 4: type checking                                                                                                                     |
print(f"Our product {product}'s type is a {type(product)}")                                                                                #   |
print(f"We have {amount} of it. The type of amount is: {type(amount)}")                                                                    #   |
amount = 90                                                    # we still have "none left" assigned, lets assign 90 again to amount            |
print(f"But we had {amount} of it. The type of amount was: {type(amount)}")                                                                #   |
print(f"One costs us {price}. The type is: {type(price)}")                                                                                 #   |
print(f"My Friend said that {product} is a fruit and it is: {is_fruit}.")                                                                  #   |
print(f"The type of is_fruit is {type(is_fruit)}")                                                                                         #   |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#Our product Apple's type is a <class 'str'>                                                                                                   |
#We have none left of it. The type of amount is: <class 'str'>                                                                                 |
#But we had 90 of it. The type of amount was: <class 'int'>                                                                                    |
#One costs us 0.55. The type is: <class 'float'>                                                                                               |
#My Friend said that Apple is a fruit and it is: True.                                                                                         |
#The type of is_fruit is <class 'bool'>                                                                                                        |
#----------------------------------------------------------------------------------------------------------------------------------------------|
