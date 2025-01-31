#---------------------------------------------------------------------------------------------------------|
# Insertion Sort: Simple algorithm that builds the final sorted list one element at a time                |
# efficient for small datasets, but still O(n²) time complexity                                           |
#---------------------------------------------------------------------------------------------------------|
def insertion_sort(values):                                            # function with list as input      |
    for i in range(1, len(values)):                                    # start from 2. element            |
        current_value = values[i]                                      # store current element to insert  |
        position = i                                                   # track current position           |
        # Shift elements greater than current value to the right                                          |
        while position > 0 and values[position-1] > current_value:     # compare with left neighbor       |
            values[position] = values[position-1]                      # shift larger element to the right|
            position -= 1                                              # move to previous position        |
        values[position] = current_value                               # insert value at correct position |
    print(values)                                                      # print sorted list                |
insertion_sort([9, 2 , 5 , 346, 456 , 234, 3345, 3, 7, 8, 9, 123, 10]) # call function                    |
#--- Terminal Output: ------------------------------------------------------------------------------------|
#[2, 3, 5, 7, 8, 9, 9, 10, 123, 234, 346, 456, 3345]                                                      |
#---------------------------------------------------------------------------------------------------------|
