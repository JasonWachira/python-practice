# defines a function that checks whether the number passed is odd or even
def check(num):
    # an even number is able to divide 2 without leaving a remainder
    if num % 2 == 0:
        return "even"
    # if it does not divide 2 exactly, the function returns odd
    return "odd"


print(check(7)) # prints odd
print(check(8)) # prints even

