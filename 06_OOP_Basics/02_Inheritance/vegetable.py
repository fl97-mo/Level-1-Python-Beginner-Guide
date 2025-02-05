from store_product import StoreProduct      

class Vegetable(StoreProduct):
    def __init__(self, name, price, origin, veg_type):  # Constructor method
        super().__init__(name, price, "Vegetable")      # Calling the constructor method of the parent class
        self.origin = origin
        self.type = veg_type
        print(f"Vegetable added: {self.name} from {self.origin} ({self.type})")

    def get_product_information(self):
        print("==Product Information========================================================")
        print(f"Name: {self.name}\nPrice per kg: {self.price}€\nOrigin: {self.origin}\nType: {self.type}")