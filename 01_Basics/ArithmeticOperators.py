# Arithmetic Operators = perform mathematical operations                                           |
# Work with numeric types, output numeric                                                          |
# Are used in nearly every code                                                                    |
# +	Addition	            6 + 2 -> 8                                                             |
# -	Subtraction	            6 - 2 -> 4                                                             |
# *	Multiplication	        6 * 2 -> 12                                                            |
# /	Division	            6 / 2 -> 3.0                                                           |
# %	Modulus (Remainder)     6 % 5 -> 1 (if you devide 6 by 5, 1 is the remainder as whole nmb)     |
# ** Exponentiation (Power)	6 ** 2 -> 36 (6*6)                                                     |
# // Floor Division	        10 // 3 -> 3 (10/3 = 3,3333 -> leave out the 0.3333 -> // = 3)         |
# // Floor Division        -10 // 3 -> 4 (if nmb negative, it rounds down to the next smaller int) |
#--------------------------------------------------------------------------------------------------|
# Basic calculator in order to showcase all operators                                              |
# You'll learn how to build a code like this later. This one is just to demonstrate how the        |
# operators work.                                                                                  |
#--------------------------------------------------------------------------------------------------|
print("Arithmetic Operators in Python")         #                                                  |                                   |
nmb_1 = float(input("Your first number: "))     # Typecasting it as float to make it easier to calc|
nmb_2 = float(input("Your second number: "))    # Userinput first and second number                |
                                                #                                                  |
menu_selection = input(f"Please select a mode:\n"# Menu selection for different modes              |
"a = Addtion (+)\n"                             #                                                  |
"b = Substraction (-)\n"                        #                                                  |
"c = Multiplicatin (*)\n"                       #                                                  |
"d = Division (/)\n"                            #                                                  |
"e = Modulus (%)\n"                             #                                                  |
"f = Expotentiation (**)\n"                     #                                                  |
"g = Floor Division (//)\n")                    #                                                  |
                                                # The following are conditional statements         |
                                                # We will discuss them in the future.              |
                                                # you can see how result is calculated here though |
if menu_selection == "a":                       # Addition                                         |
    mode = "Addition"                           #                                                  |
    result = nmb_1 + nmb_2                      #                                                  |
elif menu_selection == "b":                     # Subtraction                                      |
    mode = "Substraction"                       #                                                  |
    result = nmb_1 - nmb_2                      #                                                  |
elif menu_selection == "c":                     # Multiplication                                   |
    mode = "Multiplication"                     #                                                  |
    result = nmb_1 * nmb_2                      #                                                  |
elif menu_selection == "d":                     # Division                                         |
    mode = "Division"                           #                                                  |
    result = nmb_1 / nmb_2                      #                                                  |
elif menu_selection == "e":                     # Modulus                                          |
    mode = "Modulus"                            #                                                  |
    result = nmb_1 % nmb_2                      #                                                  |
elif menu_selection == "f":                     # Exponentiation                                   |
    mode = "Expotentiation"                     #                                                  |
    result = nmb_1 ** nmb_2                     #                                                  |
elif menu_selection == "g":                     # Floor Division                                   |
    mode = "Floor Division"                     #                                                  |
    result = nmb_1 // nmb_2                     #                                                  |
else:                                           # In case anything else was typed in the console   |
    result = "Invalid selection"                #                                                  |
print(f"The {mode} of {nmb_1} and {nmb_2} ",    # Print the result                                 |
f"is {result}")                                 #                                                  |
#--Terminal Output---------------------------------------------------------------------------------|
#Arithmetic Operators in Python                                                                    |
#Your first number: 5                                                                              |
#Your second number: 3                                                                             |
#Please select a mode:                                                                             |
#a = Addtion (+)                                                                                   |
#b = Substraction (-)                                                                              |
#c = Multiplicatin (*)                                                                             |
#d = Division (/)                                                                                  |
#e = Modulus (%)                                                                                   |
#f = Expotentiation (**)                                                                           |
#g = Floor Division (//)                                                                           |
#e                                                                                                 |
#The Modulus of 5.0 and 3.0  is 2.0                                                                |
#--------------------------------------------------------------------------------------------------|