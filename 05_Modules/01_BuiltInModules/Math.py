# Math Module in Python = Built-in module for mathematical operations                               |
# The math module includes a variety of functions for calculations                                  |
# Print(help(math)) -> to see all functions provided by the math module                             |
# I will also show you how to programme these functions. You should use the maths module in         |
# practice, but I think it is good to better understand how maths is connected to programming       |
#---------------------------------------------------------------------------------------------------|
import math                                                  # Import the math module               |
#--Common math module functions---------------------------------------------------------------------|
# 1. math.sqrt() = Find the square root of a number                                                 |
number = 81                                                  #                                      |
square_root = math.sqrt(number)                              # Calculate the square root            |
print(f"The square root of {number} is {square_root}")       # Print number                         |
# 1a looking inside math.sqrt() -- How would you programm this? ------------------------------------|
def sqrt(n):                                                 # Square root function                 |
    return n ** 0.5                                          # n^0.5 = square root                  |
#                                                                                                   |
number = 16                                                  # Definining number as 16              |
print(f"The square root of {number} is {sqrt(number)}")      # Print from our own function          |
#--Terminal Output----------------------------------------------------------------------------------|
#The square root of 81 is 9.0                                                                       |
#The square root of 16 is 4.0                                                                       |
#---------------------------------------------------------------------------------------------------|
# 2. math.pow() = Raise a number to a power                                                         |
base = 2                                                     #                                      |
exponent = 3                                                 #                                      |
result = math.pow(base, exponent)                            # Calculate 2^3 (2 raised to power 3)  |
print(f"{base} to the power of {exponent} is {result}")#                                            |
# 2a looking inside math.pow() -- How would you programm this? -------------------------------------|
def pow(base, exponent):                                     # Power function                       |
    return base ** exponent                                  # ** = to the power of                 |
#---------------------------------------------------------------------------------------------------|
number = 4                                                   # in our function = base               |
power = 3                                                    # in our function = exponent           |
print(f"{number} to the power of {power} is {pow(number, power)}") # Print statement                |
#--Terminal Output----------------------------------------------------------------------------------|
#2 to the power of 3 is 8.0                                                                         |
#4 to the power of 3 is 64                                                                          |
#---------------------------------------------------------------------------------------------------|
# 4. math.ceil() = Round up to the nearest integer  | Use math.floor() to round down                |
# if you use negative numbers, the you will achieve the opposite effect. ceil(-4.3) = -4            |
# -> meaning you round up towards zero with negative numbers                                        |
decimal = 4.3                                                # Declaring float                      |
rounded_up = math.ceil(decimal)                              # Round 4.3 up to 5                    |
print(f"{decimal} rounded up is {rounded_up}")               # Print statement                      |
# 4a looking inside math.ceil() -- How would you programm this? ------------------------------------|
def ceil(n):                                                # Round up to the nearest integer       |
    if n > int(n):                                          # if 4.3 higher than 4 (int of 4.3)     |
        return int(n) + 1                                   # return 5                              |
    else:                                                   # if not, than stay with 4              |
        int(n)                                              # (int of 4.3 = 4 so it will stay)      |
#---------------------------------------------------------------------------------------------------|
decimal = 7.2                                               # new value to decimal                  |
print(f"{decimal} rounded up is {ceil(decimal)}")           # print statement                       |
#--Terminal Output----------------------------------------------------------------------------------|
#4.3 rounded up is 5                                                                                |
#7.2 rounded up is 8                                                                                |
#---------------------------------------------------------------------------------------------------|
print(help(math))                                           # print all info about the math module  |
#===================================================================================================|