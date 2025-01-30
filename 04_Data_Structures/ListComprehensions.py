# more compact and short way of creating lists                                                          |
# easier to read                                                                                        |
# general syntax (if-else):                                                                             |
# <OUTPUT_IF_TRUE> if <CONDITION> else <OUTPUT_IF_FALSE> for ELEMENT in SEQUENCE                        |
# filtering elements (if)                                                                               |
# <EXPRESSION> for <ELEMENT> in <SEQUENCE> if <FILTER_CONDITION>                                        |
# 1. list comprehension --------------------------------------------------------------------------------|
numbers = [1, 2, 3, 4, 5]                          # list with different numbers                        |
squared = [x**2 for x in numbers]                  # <EXPRESSION> for <ELEMENT> in <SEQUENCE>           |
print(squared)                                     # print list                                         |
#--Terminal Output--------------------------------------------------------------------------------------|
#[1, 4, 9, 16, 25]                                                                                      |
# 2. conditional list comprehension --------------------------------------------------------------------|
even_numbers = [x for x in numbers if x % 2 == 0]  # <EXPR> for <ELEMENT> in <SEQUENCE> if <CONDITION>  |
print(even_numbers)                                # print even numbers                                 |
#--Terminal Output--------------------------------------------------------------------------------------|
# [2, 4]                                                                                                |
# 3. if-else in list comprehension ---------------------------------------------------------------------|
type_of_number = ["even" if x%2==0 else "odd" for x in numbers]#                                        |
print(type_of_number)   # <OUTPUT_IF_TRUE> if <CONDITION> else <OUTPUT_IF_FALSE> for ELEMENT in SEQUENCE|
#--Terminal Output--------------------------------------------------------------------------------------|
# ['odd', 'even', 'odd', 'even', 'odd']                                                                 |
# 4. list comprehension with strings -------------------------------------------------------------------|
words = ["my", "name", "is"]                       # list of words                                      |
uppercase = [word.upper() for word in words]       # <EXPRESSION> for <ELEMENT> in <SEQUENCE>           |
print(uppercase)                                   # print uppercase words                              |
# -- Terminal Output -----------------------------------------------------------------------------------|
#['MY', 'NAME', 'IS']                                                                                   |
#=======================================================================================================|