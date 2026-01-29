# Author: Dhruv

# Takes a list of numbers as input.
# Finds the second largest number in the list without using built-in sorting functions.
# Returns the second largest number.
# Prints the result.


def second_largest(lst):
    largest = lst[0]
    second = lst[0]

    for i in lst:
        if i > largest:
            second = largest
            largest = i

        elif i > second and i != largest:
            second = i
    
    return second


numbers = [10, 5, 20, 8, 15]

result = second_largest(numbers)
print("Second largest number:", result)


def largest ():
    num1 = numbers[0]
    num2 = numbers[0]

    for i in numbers:
        if (i > num1):
            num2 = num1
            num1 = i
        elif (i  > num2 and i < num1 ):
            num2 = i
            
    return num2 

numbers = [10, 5, 20, 8, 15]
print(largest())