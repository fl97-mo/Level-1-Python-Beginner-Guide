# module for basic statistical calculations                                                     |
#-----------------------------------------------------------------------------------------------|
import statistics                                       # import the statistics module          |
# 1. measures of central tendency --------------------------------------------------------------|
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                  # defining data                         |
print(statistics.mean(data))                            # mean (average)                        |
print(statistics.median(data))                          # median (middle value)                 |
print(statistics.mode([1, 2, 2, 3, 4, 4, 4, 5]))        # mode (most common value)              |
# 2. measures of spread ------------------------------------------------------------------------|
print(statistics.variance(data))                        # variance                              |
print(statistics.stdev(data))                           # standard deviation (spread of data)   |
# 3. additional functions ----------------------------------------------------------------------|
print(statistics.median_low([1, 2, 3, 4]))              # lower median for even length datasets |
print(statistics.median_high([1, 2, 3, 4]))             # higher median for even  datasets      |
# 4. Print all available functions in the module -----------------------------------------------|
print(help(statistics))                                 # print all statistics methods          |
# -- Terminal Output ---------------------------------------------------------------------------|
#5.5                                                                                            |
#5.5                                                                                            |
#4                                                                                              |
#9.166666666666666                                                                              |
#3.0276503540974917                                                                             |
#2                                                                                              |
#3                                                                                              |
#===============================================================================================|