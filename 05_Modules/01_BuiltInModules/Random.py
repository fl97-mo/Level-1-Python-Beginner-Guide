# random Module = module to generate random choices.                                                      |
#---------------------------------------------------------------------------------------------------------|
import random                                              # import the random module                     |
# 1. Generating random numbers ---------------------------------------------------------------------------|
print(random.randint(1, 10))                               # random integer between 1 and 10 (inclusive)  |
print(random.uniform(1, 10))                               # random float between 1 and 10                |
print(random.randrange(0, 100, 5))                         # random number between 0-100, step 5          |
# 2. Random choice from a list ---------------------------------------------------------------------------|
fruits = ["Apple","Banana", "Cherry", "Date", "Elderberry"]# define a list of fruits                      |
print(random.choice(fruits))                               # select a random fruit from the list          |
print(random.sample(fruits, 2))                            # select 2 unique random items                 |
print(random.choices(fruits, k=2))                         # select 2 random items (duplicates possible)  |
# 3. Shuffling a list ------------------------------------------------------------------------------------|
random.shuffle(fruits)                                     # shuffle the list in place                    |
print(fruits)                                              # print shuffled list                          |
# 4. Simulating a dice roll ------------------------------------------------------------------------------|
print(f"You rolled a {random.randint(1, 6)}")              # simulate rolling a six-sided dice            |
# 5. Print all available functions in the module ---------------------------------------------------------|
print(help(random))                                        # print all random methods                     |
# -- Terminal Output -------------------------------------------------------------------------------------|
#7                                                                                                        |
#1.7146500019957671                                                                                       |
#45                                                                                                       |
#Date                                                                                                     |
#['Elderberry', 'Apple']                                                                                  |
#['Elderberry', 'Apple']                                                                                  |
#['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']                                                      |
#You rolled a 3!                                                                                          |
#=========================================================================================================|