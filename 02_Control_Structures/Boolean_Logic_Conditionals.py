# boolean logic = True or False expressions. Used for conditions, comparisons, and logic-based decisions
# conditionals = if, elif, else. Execute code if condition is True or False
# example 1: boolean values and logical expressions -------------------------------------------------------|
true_value = True                                          # boolean values are either True or False  
false_value = False                                        # false means the condition is not met  
print(f"The type of true_value is: {type(true_value)}")    # check the type of a boolean value
print(f"The type of false_value is: {type(false_value)}")  # boolean values belong to class 'bool'
#--Terminal Output-----------------------------------------------------------------------------------------|
#The type of true_value is: <class 'bool'>
# example 2: comparison operators - compared values return True or False ----------------------------------|
a = 10
b = 20 
print(f"Is a equal to b? {a == b}")                        # == checks if two values are equal                     
print(f"Is a not equal to b? {a != b}")                    # != checks if two values are not equal             
print(f"Is a greater than b? {a > b}")                     # > checks if left value is greater than right 
print(f"Is a less than b? {a < b}")                        # < checks if left value is smaller than right
print(f"Is a greater than or equal to b? {a >= b}")        # >= checks if left is greater or equal 
print(f"Is a less than or equal to b? {a <= b}")           # <= checks if left is smaller or equal  
#--Terminal Output-----------------------------------------------------------------------------------------|
#Is a equal to b? False
#Is a not equal to b? True
#Is a greater than b? False
#Is a less than b? True
#Is a greater than or equal to b? False
#Is a less than or equal to b? True
# example 3: logical operators - used to combine *multiple* boolean expressions ---------------------------|
condition1 = True
condition2 = False
print(f"condition1 AND condition2: {condition1 and condition2}")   # and: True only if both are True
print(f"condition1 OR condition2: {condition1 or condition2}")     # or: True if at least one is True
print(f"NOT condition1: {not condition1}")                         # not: reverses the value
print(f"NOT condition2: {not condition2}")
#--Terminal Output-----------------------------------------------------------------------------------------|
#condition1 AND condition2: False
#condition1 OR condition2: True
#NOT condition1: False
#NOT condition2: True
# example 4: conditional statements -----------------------------------------------------------------------|
x = 15
if x > 10:
    print("x is greater than 10")      # runs if condition is True
elif x == 10:                                                                                                                 
    print("x is exactly 10")           # runs if previous condition was False, and this one is True
else:                                                                                                                          
    print("x is less than 10")         # runs if all previous conditions were False
#--Terminal Output-----------------------------------------------------------------------------------------|
#x is greater than 10
# example 5: combining boolean logic and conditionals -----------------------------------------------------|
age = 20 
license = True
if age >= 18 and license:
    print("You can drive.")            # both conditions must be True 
else:                                                                                                                          
    print("You cannot drive.")                                                                                                
#--Terminal Output-----------------------------------------------------------------------------------------|
#You can drive.
#----------------------------------------------------------------------------------------------------------|
