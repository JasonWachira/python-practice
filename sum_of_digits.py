# function to get the sum of digits in a number
def sum(num):
    # initialise a variable to store the sum
    total = 0

    while num > 0:
        # adds total to the remainder gotten by dividing num by 10 i.e. the last digit in the number
        total += num % 10
        # modifies num to be equal to the result of floor division by 10 which removes the last digit
        num //= 10
        # the loop runs as long as num is greater than 0 i.e. there are still digits left in the number
    return total


print(sum(12))  # prints 3
