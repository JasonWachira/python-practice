
def addElements(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total


my_list = [1,2,34,5,6,7,8,8]
print(addElements(my_list))
