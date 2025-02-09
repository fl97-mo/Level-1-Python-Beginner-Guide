# *args = work with a custom amount of arguments in a function (e.g. if you don't know the amount beforehand)
# **kwargs = work with a custom amount of key value arguments in a function (e.g. not every key value pair is required)
#---------------------------------------------------------------------------------------------------------------------
# defining regular function
# only accepts the exact number of parameters defined, providing too many or too few arguments results in an error
def product_price(amount, price):
    total = amount * price
    return total

print(product_price(23,0.5))
# Console output:
#11.5
#---------------------------------------------------------------------------------------------------------------------
# defining a function with *args
def product_name(*args):
    for i in args:                                                 # args is our iterable tuple
        print(f"{i}", end= " ")

product_name("Red", "Apple", "By Pink Lady", "Made in Australia")  # custom amount of arguments entered
print()
# Console output:
#Red Apple By Pink Lady Made in Australia
#---------------------------------------------------------------------------------------------------------------------
# defining a function with **kwargs (key:value)
def print_product_information(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_product_information(
    Name = "Banana",
    Brand = "Chiquita",
    Origin = "Columbia",
    Price = 1.65,
    InStock = 80
)
# Console output:
#Name: Banana
#Brand: Chiquita
#Origin: Columbia
#Price: 1.65
#InStock: 80
#---------------------------------------------------------------------------------------------------------------------