# function that takes an array as an argument
def addElements(arr):
    # initialises a variable that stores the sum of the elements in the array
    total = 0
    for i in range(len(arr)):
        # in each iteration, the value of total is increased by the value of arr[i]
        total += arr[i]
    return total


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(addElements(my_list)) # prints 55
