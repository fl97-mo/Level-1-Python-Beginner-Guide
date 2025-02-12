# a very popular task in coding interviews.
# assignment:
# all numbers between 1 and 100 that are divisible by three are replaced by the word Fizz 
# and all numbers that are divisible by five are replaced by the word Buzz. 
# numbers that are divisible by both three and five should output FizzBuzz.

for i in range (1,101):         # remember, the second number is exclusive
    word = ""
    if i % 3 == 0:
        word += "Fizz"
    if i % 5 == 0:
        word += "Buzz"
    print(f"{i}: {word}")
    

