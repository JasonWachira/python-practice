# Python-Practice
## Jason Wachira Kamwaro - 172995
## 1. Sum All Elements In a List
Function definition specifying an argument called arr
```python
def addElements(arr):
```
Initialising a variable that stores the sum of the elements
```python
total = 0
```
Define a loop to iterate over all elements in the list
```python
for i in range(len(arr)):
```
Add the value of arr[i] to the total variable
```python
total += arr[i]
```
## 2. Check if a number is odd or even
Function definition
```python
def check(num):
```
A number is even if it divides 2 perfectly i.e. the remainder after division is 0. We use this property to determine if the number is odd or even.
```python
if num % 2 == 0:
    return "even"
```
## 3. Factorial using a loop
Function definition
```python
def fact(num):
```
Initialising a variable to store the factorial
```python
factorial = 1
```
Defined a loop that iterates until it reaches num
```python
for i in range(num+1):
```
This ensures that the factorial of 0 is 1

```python
if i == 0:
    factorial = 1
```
This part multiplies the current value of factorial by i
```python
else:
    factorial *= i
```
The function then returns factorial
```python
return factorial
```
## 4. Reversing a string
The function takes in the string to be reversed as input.
It then initialises an empty string to store the reversed string.

``` python 
new_string = "" "
```


We then calculate the length of the string using len(str) that will enable us to traverse the string backwards.

```python
length = len(string)-1 
 ```
We subtract 1 from the length since array indexing starts from 0.
In each iteration, we concatenate the empty string with the character at string[length]
We then decrement length by 1
```python
while length >= 0:
    new_string += string[length]
    length -= 1
```
The function returns the newly formed string

````python
return new_string
````

## 5. Recursive factorial
We define the function
```python
def factorial(num):
```
We add a condition that returns an error message if a negative number is passed.
```python
if num < 0:
    return "Cannot compute factorial of negative numbers"
```
We define the base case in order to exit the recursion
```python
if num == 0:
    return 1
```
We then implement the recursive call
```python
return num * factorial(num-1)
```

## 6. Sum of digits in a number
The function initialises an empty variable to store the sum.
```python
total=0
``` 

A loop that runs as long as num is greater than 0


```python 
while num > 0:
```

this,

```python
total += num % 10
```

is the shorthand for:

```python
total = total + num % 10
```

which adds the total to the remainder of num / 10. This adds the remainder i.e. the last digit in the number to the total variable.

```python
num //= 10 
``` 

is the shorthand for 

```python
num = num // 10
```

which essentially 'removes' the last digit since in python, floor division ignores the remainder and leaves only the whole number part.
This ensures that the loop terminates since it reaches a point whereby num will reach 0.
The function then returns total

```python
return total
```