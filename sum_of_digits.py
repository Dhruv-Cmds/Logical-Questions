# Author: Dhruv

# Takes a number as input.
# Calculates the sum of its digits.
# Returns the sum.
# Prints the result.

def sum_of_digits(n):
    total = 0
    for i in str(n):
        total += int(i)

    return total

n = int(input("value enter :"))
print(sum_of_digits(n))