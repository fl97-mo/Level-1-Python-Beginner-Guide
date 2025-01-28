# demonstration of the custom Supermarket module
# import the functions from the Supermarket module
import Supermarket

# lets buy some apples
product_name = "Apple"
price_per_item = 0.5
quantity = 10

print(Supermarket.calculate_total_price(price_per_item, quantity))
Supermarket.greet_customer()
print(help(Supermarket))
#The total is: 5.00€
#Hello and welcome to our Supermarket, have fun and spend all your money!
#Help on module Supermarket:
#...