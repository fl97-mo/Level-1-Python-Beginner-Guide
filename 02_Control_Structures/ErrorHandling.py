# error handling in Python = handling of errors. ensures that the programme does not crash.         |
# manage the Erorrs, offer alternatives to users                                                    |
# 1. try-except ------------------------------------------------------------------------------------|
# example: asking the user for the price of an item                                                 |
try:                                                               # try statement                  |
    price = float(input("Enter the price of the product: "))       # convert input to float         |
    print(f"The price is {price}€")                                # print price                    |
except ValueError:                                                 # handle invalid input           |
    print("Invalid input! Please enter a valid price.")            # inform user of error           |
# -- Terminal Output -------------------------------------------------------------------------------|
#Enter the price of the product: hello                                                              |
#Invalid input! Please enter a valid price.                                                         |
#Enter the total stock of the product:                                                              |
# 2. multiple exceptions ---------------------------------------------------------------------------|
# example: calculating the total cost of veggies based on weight                                    |
try:                                                               # try statement                  |
    price_per_kg = float(input("Enter the price per kilo in €: ")) # input price                    |
    weight = float(input("How much does your vegetable weight? ")) # input weight                   |
    total_price = price_per_kg * weight                            # calculate total                |
    print(f"The cost for {weight:.2f} kg is {total_price:.2f}€.")  # print result                   |
except ValueError:                                                 # handle invalid input           |
    print("Invalid input! Please enter a number")                  # inform user                    |
except Exception as e:                                             # catch unexpected errors as var.|
    print(f"An unexpected error occurred: {e}")                    # print error message            |
# -- Terminal Output -------------------------------------------------------------------------------|
#Invalid input! Please enter a valid price.                                                         |
#Enter the price per kilo in €: 2                                                                   |
#How much does your vegetable weight? q                                                             |
#Invalid input! Please enter a number                                                               |
# 3. multiple exceptions & ZeroDivisionError -------------------------------------------------------|
# example: average sales per day                                                                    |
try:                                                               # try statement                  |
    total_sales = int(input("Total items sold?: "))                # input total sales              |
    days = int(input("In how many days?: "))                       # input days                     |
    avg_sales = total_sales / days                                 # calculate average              |
    print(f"Average sales per day: {avg_sales:.2f}x items.")       # print result                   |
except ValueError:                                                 # handle invalid input           |
    print("Invalid input! Please enter whole numbers only.")       # inform user                    |
except ZeroDivisionError:                                          # handle division by zero        |
    print("Cannot divide by zero!")                                # inform user                    |
# -- Terminal Output -------------------------------------------------------------------------------|
#Total items sold?: 2000                                                                            |
#In how many days?: 0                                                                               |
#Cannot divide by zero!                                                                             |
# 4. else and finally blocks -----------------------------------------------------------------------|
# example: adding items to the shopping cart                                                        |
shopping_cart = []                                                 # list for shopping cart         |
try:                                                               # try statement                  |
    product = input("Enter the product name: ")                    # input product name             |
    if not product:                                                # check if input is empty        |
        raise ValueError("Product name cannot be empty!")          # raise error if empty           |
    shopping_cart.append(product)                                  # add product to the cart        |
    print(f"{product} added to the cart.")                         # confirm added product          |
except ValueError as e:                                            # handle empty input             |
    print(f"Error: {e}")                                           # print error message            |
else:                                                              # if no exceptions occurred      |
    print("Item successfully added to your cart.")                 # confirm added item             |
finally:                                                           # always executed                |
    print("Shopping cart process finished.")                       # end of process                 |
# -- Terminal Output -------------------------------------------------------------------------------|
#Enter the product name:                                                                            |
#Error: Product name cannot be empty!                                                               | 
#Shopping cart process finished.                                                                    |
#---------------------------------------------------------------------------------------------------|
