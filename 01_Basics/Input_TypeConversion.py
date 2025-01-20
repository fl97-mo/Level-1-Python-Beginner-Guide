# Input and Type Conversion in Python                                                               |
# Two smaller but important topics covered in one file                                              |
#===================================================================================================|
# Input = Get user input                                                                            |
# The input is ALWAYS stored as a string by default, regardless of what the user types.             |
#---------------------------------------------------------------------------------------------------|
product = input("What is the products name? ")          # User enters a string                      |
print(product)                                          # Printing input, stored in a variable      |
#                                                                                                   |
print(type(product))                                    # Use type() to check the type of variable  |
amount = input("How many do you want to buy? ")         # Input will still be handled as String     |
print(amount)                                           # Print the Input                           |
print(type(amount))                                     # Show type of amount                       |
#--Terminal Output----------------------------------------------------------------------------------|
#What is the products name? Kiwi                        -> User Input: Kiwi                         |
#Kiwi                                                                                               |
#<class 'str'>                                                                                      |
#How many do you want to buy? 5                         -> User Input: 5                            |
#5                                                                                                  |
#<class 'str'>                                          -> Still a String type                      |
#---------------------------------------------------------------------------------------------------|
# And what is the problem that it is still a String? You can tell it is a 5 and 5 is a number?      |
# - yes, we automatically translate it into a number, but the computer sees "5" as just a character,|
# like "?" or "m". It doesn't understand its numeric value. Thats why you need to convert the type. |
# In our case, into an Integer. Because you can't buy 2.00034 Kiwis but buy full numbers of it.     |
# We also can't calculate with strings. "5" + "5" = 55 and not 10.                                  |
#===================================================================================================|
# Type conversion = Convert data from one type to another                                           |
# Using built-in functions like int(), float(), str()                                               |
#-Integer-------------------------------------------------------------------------------------------|
amount = int(input("How many do you want to buy? "))    # Convert string input to integer by int()  |
print(amount)                                           # Print the Input                           |
print(type(amount))                                     # Display the type                          |
#-Float---------------------------------------------------------------------------------------------|
price = float(input("How much does it cost? "))         # Convert string input to float by float()  |
print(price)                                            # Print the input                           |
print(type(price))                                      # Display the type                          |
#-String--------------------------------------------------------------------------------------------|
name = "Flo"                                            # Name in string                            |
year_of_birth = 1997                                    # the year is an integer                    |
# username = name + year_of_birth   ! Type Error !      # 'Username generator'                      |
# print(Username)                                       # You cant combine string and int           |
username = name + str(year_of_birth)                    # Int converted to string                   |
print(username)                                         # Now it is printable                       |
#--Terminal Output----------------------------------------------------------------------------------|
#How many do you want to buy? 4                         -> userinput 4 converted to int             |
#4                                                                                                  |
#<class 'int'>                                                                                      |
#How much does it cost? 1.25                            -> userinput 1.25 converted to float        |
#1.25                                                                                               |
#<class 'float'>                                                                                    |
#Flo1997                                                -> int converted into string for username   |
#---------------------------------------------------------------------------------------------------|