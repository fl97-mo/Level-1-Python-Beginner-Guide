# you can also create costum modules.                                                   |
# they work exactly as Built in Modules                                                 |
# define reusable functions, use them in other scripts                                  |
# with 3x" ("""abcde""") you create docstrings                                          |
# docstrings are used for do cumentation of your methods. You can later call them       | 
# with the help() module                                                                |
#---------------------------------------------------------------------------------------|
def calculate_total_price(price_per_item, quantity):                #                   |
    """Calculates the total price for a given quantity of items.""" #docstring          |      
    total = price_per_item * quantity                               #                   |
    return f"The total is: {total:,.2f}€"                           #                   |
#---------------------------------------------------------------------------------------|
def greet_customer():                                               #                   |
    """Greets our Customers according to company standards"""       #                   |
    print("Hello and welcome to our Supermarket, have fun and spend all your money!")  #|
#---------------------------------------------------------------------------------------|