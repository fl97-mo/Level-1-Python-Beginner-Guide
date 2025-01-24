# Strings = Immutable sequences of characters used to store text. "apple" = 'a'+'p'+'p'...    |
# "Immutable" = Strings cannot be changed directly; any modification creates a new string.    |
# You can perform various operations such as slicing, chaining and applying methods.          |
# Strings are one of the most commonly used data types in Python.                             |
# 1. Basic String Creation and Indexing ------------------------------------------------------|
text = "Hello World!"                                 # Define a string                       |
print(text)                                           # Print the string                      |
print(text[0])                                        # Access the first character ('P')      |
print(text[-1])                                       # Access the last character ('!')       |
# 0 = starting index in general and -1 = last character, object etc.                          |
# -- Terminal Output -------------------------------------------------------------------------|
# Hello World!                                                                                |
# H                                                                                           |
# !                                                                                           |
# 2. String slicing --------------------------------------------------------------------------|
print(text[1:3])                                       # Slice from index 1 to 3              |
print(text[:2])                                        # starting from 0, ending at 2         |
print(text[1:])                                        # Slice from index 1 to the end        |
print(text[::4])                                       # Step by 4, skipping every second char|
# -- Terminal Output -------------------------------------------------------------------------|
# el                                                                                          |
# He                                                                                          |
# ello World!                                                                                 |
# Hor                                                                                         |
# 3. String chaining ---- --------------------------------------------------------------------|
first_name = "Erika"                                   # Define first name                    |
last_name = "Mustermann"                               # Define last name                     |
full_name = first_name + " " + last_name               # Combine with a space in between      |
print(full_name)                                       # Print the full name                  |
# -- Terminal Output -------------------------------------------------------------------------|
# Erika Mustermann                                                                            |
# 4. String Methods --------------------------------------------------------------------------|
print(text.lower())                                    # All to lowercase                     |
print(text.upper())                                    # All to uppercase                     |
print(text.replace("Hello", "Hi"))                     # Replace substring                    |
print(text.split())                                    # Split string into words              |
print("-".join(["Bye", "Bye"]))                        # Connect words with a hyphen          |
# -- Terminal Output -------------------------------------------------------------------------|
# hello world!                                                                                |
# HELLO WORLD!                                                                                |
# Hi World!                                                                                   |
# ['Hello', 'World!']                                                                         |
# Bye-Bye                                                                                     |
# 5. String Formatting -----------------------------------------------------------------------|
name = "Erika"                                         # Define a name                        |
age = 45                                               # Define an age                        |
print(f"My name is {name}, and I am {age} years old.") # f-strings for formatted output       |
print("My name is {}, and I am {} years old.".format(name, age)) # .format() method           |
# -- Terminal Output -------------------------------------------------------------------------|
#My name is Erika, and I am 45 years old.                                                     |
#My name is Erika, and I am 45 years old.                                                     |
# 6. Checking String Properties --------------------------------------------------------------|
print(text.startswith("Hello"))                        # Check if string starts with "Hello"  |
print(text.endswith("Planet"))                         # Check if string ends with "Planet"   |
print(text.endswith("!"))                              # Check if string ends with "!"        |
print("Wor" in text)                                   # Check if substring is in string      |
# -- Terminal Output -------------------------------------------------------------------------|
# True                                                                                        |
# False                                                                                       |
# True                                                                                        |
# True                                                                                        |
# 7. Escape Characters -----------------------------------------------------------------------|
quote = "I said, \"Hello World!\""                     # Use \" to include double quotes      |
path = "C:\\Users\\Name\\Documents"                    # Use \\ for backslashes in paths      |
print(quote)                                           # Print quote                          |
print(path)                                            # Print file path                      |
# -- Terminal Output -------------------------------------------------------------------------|
#I said, "Hello World!"                                                                       |
#C:\Users\Name\Documents                                                                      |
#------------------------------------------------------------------------------------------------|

