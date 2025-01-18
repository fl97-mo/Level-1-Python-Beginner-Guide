# sorting algorithms: sort values in a specific order, eg. bubble sort, quick sort,...                     |
# bubble sort: one of the easier to implement, but inefficient for bigger lists O(n²)                      |
# compares an element with its right neighbor                                                              |
# if neighbor "lower", switch with the neighbor                                                            |
# repeat until list sorted                                                                                 |
# the list is sorted in place, meaning your original list will be modified                                 |
#-Example:-------------------------------------------------------------------------------------------------|
# declaring a sort fuction                                                                                 |
def bubble_sort(values):                                               # function with list as input       |
    is_sorted = False                                                  # checks if list is sorted          |
    while is_sorted == False:                                          # run until no swaps needed         |
        is_sorted = True                                               # assume the list is sorted         |
        for i in range(len(values) - 1):                               # loop through until 2nd-last item  |
            if values[i] > values[i+1]:                                # if current item > next item       |
                values[i], values[i+1] = values[i+1], values[i]        # swap items                        |
                is_sorted = False                                      # set to false, since we needed swap|
    print(values)                                                      # print sorted list                 |
#-Calling function in Code later --------------------------------------------------------------------------|
bubble_sort([1,2,7,5,4,7,9,10,23,1231,12,563,34,346,364,31,12,3,8,23]) # call function                     |
#-Terminal Output------------------------------------------------------------------------------------------|
# [1, 2, 3, 4, 5, 7, 7, 8, 9, 10, 12, 12, 23, 23, 31, 34, 346, 364, 563, 1231]                             |
#----------------------------------------------------------------------------------------------------------|