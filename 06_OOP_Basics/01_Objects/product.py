class Product:                                                      # Defining Class Product                     |
    amount_of_products = 0                                          # Class variable = above constructor         |
                                                                                                                #|
    def __init__(self,brand, type, price, amount_stocked):          # # Constructor with variables; self refers  |
                                                                    # to current instance = to your specific obj.|
        self.brand = brand                                          # Exmpl. your (brand) "Pink Lady" will be    |
                                                                    # saved in (self.brand)                      |
        self.type = type                                                                                        #|
        self.price = price                                                                                      #|
        self.amount_stocked = amount_stocked                                                                    #|
                                                                                                                #|
        Product.amount_of_products += 1                             # Increment class variable by one per        |
                                                                    # product added                              |
        print(f"Product added: {self.type} by {self.brand}")        # print current object                       |
                                                                    # e.g. "product1"                            |
    def get_product_information(self):                              # define a method. refer it to self.         |
        print(f"==Product=Information=========================================================================="#|
            f"\nType: {self.type}"                                                                              #|
            f"\nBrand: {self.brand}"                                                                            #|
            f"\nPrice: {self.price}€"                                                                           #|
            f"\nAmount stocked: {self.amount_stocked}")                                                         #|
                                                                                                                #|
    def product_availability(self):                                 # define a method. refer it to self.         |
        print("==Product=Availabilty==========================================================================")#|
        if self.amount_stocked > 0:                                 # if we have more than one, then available   |
            print(f"{self.type}'s by {self.brand} are available.")                                              #|
        else:                                                       # if not, then not available                #|
            print(f"{self.type}'s by {self.brand} not available.")                                              #|
                                                                    # You want to create a class method reffering|
                                                                    # to a class variable. you need to put the   |
    @classmethod                                                    # decorator @classmethod before your method  |
    def products_in_total(cls):                                     # define a method. refor to class itself     |
        print("==Product=Variaty==============================================================================")#|
        print(f"We have {cls.amount_of_products} different products in our store.") #cls. -> refering to class   |
#----------------------------------------------------------------------------------------------------------------|