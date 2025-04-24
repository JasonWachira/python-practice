def fact(num):
    # initialises the factorial variable that stores the factorial on each iteration
    factorial = 1
    # loop starts at 1,2,3...num. it stops right before num+1 which is at num
    for i in range(1, num + 1):
        # shorthand for writing factorial = factorial * i which is the loop counter
        factorial *= i
    return factorial


print(fact(5)) # prints 120
