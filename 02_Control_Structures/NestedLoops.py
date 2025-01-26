# nested loop = a loop inside a loop                                                                       |
# used to process multi-dimensional data structures like tables, matrices etc.                             |
# outer loop = sets number of iterations of inner loop                                                     |
# inner loop = restarts with every iteration of the outer loop                                             |
#                                                                                                          |
#-- 1) printing a square ----------------------------------------------------------------------------------|
rows = 3                                    # setting up amount of rows                                    |
columns = 4                                 # setting up amount of colums                                  |
                                            # row itself->value of 3; not iterable; range of 3 is iterable |
for row in range(rows):                     # outer loop, ('how often should the inner loop execute')      |
    for column in range(columns):           # inner loop, ('Do this ‘outer loop’-times)                    |
        print("[]",end= "")                 # inner loop prints []. end= "" -> to avoid a line break       |
    print ()                                # new line each time outer loop executes                       |
#--Terminal Output-----------------------------------------------------------------------------------------|
#[][][][]                                                                                                  |
#[][][][]                                                                                                  |
#[][][][]                                                                                                  |
#                                                                                                          |
#-- 2) iterating over shopping cart -----------------------------------------------------------------------|
shopping_cart = [                                       #                                                  |
    {"name": "Apple", "price": 0.50, "amount": 3},      # products with prices and amounts we buy          |
    {"name": "Banana", "price": 0.45, "amount": 6},     #                                                  |
    {"name": "Carrot", "price": 0.29, "amount": 10},    #                                                  |
]                                                       #                                                  |
for product in shopping_cart:               # outer loop, iterating through each dictionary in the list    |
    for key, value in product.items():      # inner loop, iterating through key-value pairs of each product|
        print(f"{key}: {value}")            # print key and value of the current product                   |
    print()                                 # new line per product                                         |
#--Terminal Output-----------------------------------------------------------------------------------------|
#name: Apple                                                                                               |
#price: 0.5                                                                                                |
#amount: 3                                                                                                 |
#                                                                                                          |
#name: Banana                                                                                              |
#price: 0.45                                                                                               |
#amount: 6                                                                                                 |
#                                                                                                          |
#name: Carrot                                                                                              |
#price: 0.29                                                                                               |
#amount: 10                                                                                                |
#                                                                                                          |
#-- 3) 2d matrix - multiplication table--------------------------------------------------------------------|
rows = 5                                    # defining the rows                                            |
columns = 15                                # defining amount of colums                                    |
for row in range(1, rows + 1):              # inner loop, range(1, rows +1) because indexing starts at 0   |
    for column in range(1, columns + 1):    # outer loop, same aplies here as well                         |
        print (row * column, end= " ")      # multiply amount of row with values of the colums             |
    print()                                 # new line each outer loop                                     |
#--Terminal Output-----------------------------------------------------------------------------------------|
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15                                                                       |
#2 4 6 8 10 12 14 16 18 20 22 24 26 28 30                                                                  |
#3 6 9 12 15 18 21 24 27 30 33 36 39 42 45                                                                 |
#4 8 12 16 20 24 28 32 36 40 44 48 52 56 60                                                                |
#5 10 15 20 25 30 35 40 45 50 55 60 65 70 75                                                               |
#==========================================================================================================|