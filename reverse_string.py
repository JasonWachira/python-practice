def reverse(string):
    # initialise an empty string to store the reversed string
    new_string = " "
    # initialise a counter that starts from the end of the string-1 since arrays start counting from 0
    length = len(string) - 1
    while length >= 0:
        # concatenate the new string with the old string[length]
        new_string += string[length]
        # decrease length by 1 to go to the previous character in string
        length -= 1
    return new_string


print(reverse("Hello"))  # prints olleH
