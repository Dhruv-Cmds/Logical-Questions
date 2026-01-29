# Author: Dhruv

# Takes two numbers from the user.
# Takes an arithmetic operation (+, -, *, /) as input.
# Uses a function to perform the selected operation on the two numbers.
# Returns the result from the function.
# Displays the final answer to the user.


def calculator (a , b , operation):
    if (operation == "+") :
        return a + b 
    
    elif (operation == "-") :
        return a - b
    
    elif (operation == "*") :
        return a * b
    
    elif (operation == "/") :
        return a / b

a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
operation = input("Enter operation :")

print(f"Answer of {a} and {b} is using {operation} {calculator(a , b , operation)} :")