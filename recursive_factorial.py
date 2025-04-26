# a function that calculates the factorial of a number using recursion
def factorial(num):
    # Returns a message when trying to compute factorial of negative numbers
    if num < 0:
        return "Cannot compute factorial of negative numbers"
    # base case for determining exiting from the recursion. when the recursive call reaches 0 it returns 1 since 0! = 1
    if num == 0:
        return 1
    # recursively solves the factorial by taking the current
    # recursive call's num and multiplying it with the factorial of the previous number all the way up to zero
    return num * factorial(num - 1)


print(factorial(5))  # prints 120

print(factorial(-1)) # prints out 'Cannot compute factorial of negative numbers'
