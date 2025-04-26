def fact(num):
<<<<<<< HEAD
    # Checks if a negative number has been passed and returns an error message
=======
    # Checks if a negative number has been passed and returns an error message
>>>>>>> 4913c294d6f4e5857042482ffd8b1852feb7397a
    if num < 0:
        return "Cannot compute factorial of negative numbers"
    # initialises the factorial variable that stores the factorial on each iteration
    factorial = 1
    # loop starts at 1,2,3...num. it stops right before num+1 which is at num
    for i in range(1, num + 1):
        # shorthand for writing factorial = factorial * i which is the loop counter
        factorial *= i
    return factorial


print(fact(5)) # prints 120
