# Why use functions?                                                                                                                           |
# Functions allow you to use the same code multiple times.                                                                                     |
# They make your code more organized and easier to understand.                                                                                 |
# Changes can be made in the function, you wont need to change every instance in the code.                                                     |
# function = A block of reusable code, you define it with def and use it with()                                                                |
# Parameters are flexible and can accept different data types (e.g., strings, floats, booleans).                                               |
#----------------------------------------------------------------------------------------------------------------------------------------------|
#                                                                                                                                              |
# task 1: Define a simple function.                                                                                                            |
#                                                                                                                                              |
#--Defining the function-----------------------------------------------------------------------------------------------------------------------|
def hello_world():                                              # define function(): <- how you define a function                              |
    print("Hello World!")                                       # inside the function you write what the function does                         |
#--Calling function----------------------------------------------------------------------------------------------------------------------------|
hello_world()                                                   # once the function is defined, you can call it throughout the programm        |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#Hello World!                                                   # output of the function. hi there again                                       |
#----------------------------------------------------------------------------------------------------------------------------------------------|
#                                                                                                                                              |
#  task 2: Review a Product with two parameters. Parameters act as placeholders for values                                                     |
#  They allow you to pass diffrent values into the fuction when you call it                                                                    |
#--Defining the function-----------------------------------------------------------------------------------------------------------------------|
def product_overview(name, price):                              # define product_overview(parameter1, parameter2,...):                         |
    print(f"The product {name} costs {price:,.2f}€.")           # Use f-string formatting to display passed parameters.                        |
                                                                # {parameter1:,.2f} ensures thousands separators and 2 decimal places          |
#--Calling function----------------------------------------------------------------------------------------------------------------------------|
product_overview("Car", 19500.75)                               # Calling product_overview with specific arguments (parameter1,parameter2)     |
                                                                # Arguments replace placeholders in the function                               |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#The product Car costs 19,500.75€.                                                                                                             |
#----------------------------------------------------------------------------------------------------------------------------------------------|
#                                                                                                                                              |
# return = is used to send a value back, from the function where it was called                                                                 |
# task 3: Calculate the total cost of a product by multiplying its price by amount purchased.                                                  |
#                                                                                                                                              |
#--Defining the function-----------------------------------------------------------------------------------------------------------------------|
def cost_of_product(price, amount):                             # define cost_of_product                                                       |
    total = price * amount                                      # total is defined here                                                        |
    return total                                                # if you call this function, total will be returned                            |
#--Calling function----------------------------------------------------------------------------------------------------------------------------|
print(f"The total is {cost_of_product( 0.5, 500):,.2f}€.")      # you can call functions within a f-string. Again with euro formating          |
                                                                # withing {} our {total} will be returned, if price and amount is defined      |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#The total is 250.00€.                                                                                                                         |
#----------------------------------------------------------------------------------------------------------------------------------------------|
#                                                                                                                                              |
# task 3: Ask for user input (name, price, amount) and display the product and total in the terminal. Use the right formats.                   |
#                                                                                                                                              |
#--Defining the function-----------------------------------------------------------------------------------------------------------------------|
def name_price_of_product():                                    # defined function. parameters will be defined within, not when you call it    |
    name   = input("What product do you want to purchase?: ")   # input = always per default in string, so no need to change format            |
    price  = float(input("How much does your product cost?: ")) # float(input()) -> converts your string input into a float number             |
    amount = int(input("How many do you want to purchase?: "))  # int(input()) -> converts the input into an integer                           |
    total = price * amount                                      # defining 'total'                                                             |
    print(f"You bought {amount}x of {name}'s.")                 # f-string displaying amount and product name                                  |
    print(f"Your total will be {total:,.2f}€.")                 # displaying and formating the total                                           |
#--Calling function----------------------------------------------------------------------------------------------------------------------------|
name_price_of_product()                                         # no need to put values inside the function, since we will define them within  |
#--Terminal Output-----------------------------------------------------------------------------------------------------------------------------|
#What product do you want to purchase?: Apple                                                                                                  |
#How much does your product cost?: 0.5                                                                                                         |
#How many do you want to purchase?: 1234                                                                                                       |
#You bought 1234x of Apple's.                                                                                                                  |
#Your total will be 617.00€.                                                                                                                   |
#----------------------------------------------------------------------------------------------------------------------------------------------|
