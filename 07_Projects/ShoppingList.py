ShoppingList = []  # The global shopping list

# Function to print the list
def showList():
    if ShoppingList:
        for index, item in enumerate(ShoppingList, start=1):
            print(f"{index}. {item[0]} - {item[1]} pieces at {item[2]:.2f} € each")
    else:
        print("The list is empty.")

# Main program
while True:
    try:
        menuSelection = int(input(
            "**********\nYour Shopping List\n\n1: Add a new product\n2: Show products\n3: Remove a product from the list\n4: Calculate total cost\n5: Exit program\n**********\nYour choice: "
        ))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if menuSelection == 1:  # Add a product
        productName = input("What product would you like to add? ")
        amountOfProduct = int(input("How many are you buying? "))
        price = float(input("What is the price of the product? "))
        ShoppingList.append([productName, amountOfProduct, price])
        print(f"Your product has been added: {ShoppingList[-1]}")

    elif menuSelection == 2:  # Show products
        showList()

    elif menuSelection == 3:  # Remove a product
        showList()
        try:
            itemIndex = int(input("Which entry would you like to remove? ")) - 1
            if 0 <= itemIndex < len(ShoppingList):
                deleted_item = ShoppingList.pop(itemIndex)
                print(f"'{deleted_item[0]}' has been removed.")
            else:
                print("Invalid input.")
        except ValueError:
            print("Please enter a valid number.")

    elif menuSelection == 4:  # Calculate total cost
        if ShoppingList:
            SumEverything = 0
            for item in ShoppingList:
                amount = item[1]
                price_per_unit = item[2]
                total_per_item = amount * price_per_unit
                print(f"{item[0]}: {amount} pieces at {price_per_unit:.2f} € each = {total_per_item:.2f} €")
                SumEverything += total_per_item
            print(f"The total cost of your shopping list is: {SumEverything:.2f} €.")
        else:
            print("The shopping list is empty.")

    elif menuSelection == 5:  # Exit program
        print("Program exited.")
        break

    else:
        print("Invalid selection. Please choose between 1 and 5.")
