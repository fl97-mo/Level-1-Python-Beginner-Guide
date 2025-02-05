class StoreProduct:
    amount_of_products = 0

    def __init__(self, name, price, brand):      # Constructor method
        self.name = name
        self.price = price
        self.brand = brand
        StoreProduct.amount_of_products += 1
        print(f"Product added: {self.name} - {self.brand}")

    def get_product_information(self):          # Method to print product information#  
        print("==Product Information========================================================")
        print(f"Name: {self.name}\nPrice: {self.price}€\nBrand: {self.brand}")

    @classmethod                                # Class method to print the total amount
    def products_in_total(cls):                 # of products in the store
        print("==Product Variety============================================================")
        print(f"We have {cls.amount_of_products} different products in our store.")