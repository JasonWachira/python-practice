def fact(num):
    if num < 0:
        return "Cannot compute factorial of negative numbers"
    # initialises the factorial variable that stores the factorial on each iteration
    factorial = 1
    # loop starts at 1,2,3...num. it stops right before num+1 which is at num
    for i in range(num + 1):
        if i == 0:
            factorial = 1
        else:
            # shorthand for writing factorial = factorial * i which is the loop counter
            factorial *= i
    return factorial


print(fact(5)) # prints 120
