name = input("What is the name of your product?\n")
quantity = int(input("How many do you have?\n"))
price = float(input("What is the price of your product?\n"))

menu_selection = input("Choose an option. a) Calculate the total price b) Add Tax c) Goodbye message")

if menu_selection == "a":
    total_price = quantity * price
    print("The total price is: ")
    print(total_price, "€")
elif menu_selection == "b":
    total_price = quantity * price * 1.19 
    print("The total price with tax is: ")
    print(total_price, "€")
elif menu_selection == "c":
    print("Goodbye! See you soon!")
else:
    print("Please select a valid option: a, b or c")
