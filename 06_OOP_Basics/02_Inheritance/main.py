from store_product import StoreProduct      # Importing the StoreProduct class from store_product.py
from vegetable import Vegetable             # Importing the Vegetable class from vegetable.py

product1 = StoreProduct("Apple", 0.80, "Pink Lady") # Creating instances of the StoreProduct class
product2 = StoreProduct("Banana", 1.00, "Chiquita") 

vegetable1 = Vegetable("Carrot", 2.50, "Germany", "Organic")    # Creating instances of the Vegetable class
vegetable2 = Vegetable("Potato", 1.20, "Netherlands", "Conventional")

product1.get_product_information()      # Calling the get_product_information method of the StoreProduct class
vegetable1.get_product_information()    # Calling the get_product_information method of the Vegetable class

StoreProduct.products_in_total()        # Calling the products_in_total method of the StoreProduct class
#--Terminal Output-------------------------------------------------------------
#Product added: Apple - Pink Lady
#Product added: Banana - Chiquita
#Product added: Carrot - Vegetable
#Vegetable added: Carrot from Germany (Organic)
#Product added: Potato - Vegetable
#Vegetable added: Potato from Netherlands (Conventional)
#==Product Information========================================================
#Name: Apple
#Price: 0.8€
#Brand: Pink Lady
#==Product Information========================================================
#Name: Carrot
#Price per kg: 2.5€
#Origin: Germany
#Type: Organic
#==Product Variety============================================================
#We have 4 different products in our store.