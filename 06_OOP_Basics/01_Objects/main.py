from product import Product                             # Import class Product                  |
#                  |brand    | type  | price| amount_stocked)  -> from constructor              |
product1 = Product("Pink Lady","Apple", 0.80, 50)       # product1 initiated                    |
product2 = Product("Chiquita", "Banana", 1.00, 75)      # product2 initiated                    |
product3 = Product("McCain", "Fries", 2.59, 25)         # product3 initiated                    |
product4 = Product("Orbit", "Chewing Gum", 1.19, 250)   # product4 initiated                    |
#                                                                                               |
product3.get_product_information()                      # calling .get_product_information()    |
product4.product_availability()                         # calling .product_availability()       |
Product.products_in_total()                             # calling .products_in_total()          |
                                                        # !Class variable, not object var.!     |
#--Terminal Output------------------------------------------------------------------------------|
#Product added: Apple by Pink Lady                                                              |
#Product added: Banana by Chiquita                                                              |
#Product added: Fries by McCain                                                                 |
#Product added: Chewing Gum by Orbit                                                            |
#==Product=Information==========================================================================|
#Type: Fries                                                                                    |
#Brand: McCain                                                                                  |
#Price: 2.59€                                                                                   |
#Amount stocked: 25                                                                             |
#==Product=Availabilty==========================================================================|
#Chewing Gum's by Orbit are available.                                                          |
#==Product=Variaty==============================================================================|
#We have 4 different products in our store.                                                     |
#-----------------------------------------------------------------------------------------------|