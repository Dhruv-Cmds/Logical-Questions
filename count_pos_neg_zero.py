# Author: Dhruv

# Takes 10 numbers from the user using a loop
# Stores them in a list
# Using another loop:
# find how many numbers are positive
# how many are negative
# how many are zero
# Print:
# Positive numbers = X
# Negative numbers = Y
# Zero numbers = Z

l = []
for i in range (10):
    number = int(input("Enter a number :"))
    l.append(number)

positive_numbers = 0
negative_numbers = 0
zero_numbers = 0

for i in l :
    if (i == 0):
        zero_numbers += 1

    elif (i > 0):
        positive_numbers += 1

    else:
       negative_numbers += 1

print("Total positive numbers are :" , positive_numbers)
print("Total negative numbers are :" , negative_numbers)
print("Total zero numbers are :" , zero_numbers)

'''most imp thing is if smth wants to store no comparision needed , 
if smth comarision needed than take list set dict accroding questions'''

                        #  SECOUND METHOD

def finder (n):

    numbers = []

    for i in range (n):
        user_numbers = int(input("Enter a number to store in list :"))
        numbers.append(user_numbers)

    positive_numbers = 0
    negative_numbers = 0
    zero_numbers = 0

    for i in numbers:

        if (i == 0):
            zero_numbers += 1

        elif (i > 0):
            positive_numbers += 1
        
        elif (i < 0):
            negative_numbers += 1

    print("Total positive numbers are :" , positive_numbers)
    print("Total negative numbers are :" , negative_numbers)
    print("Total zero numbers are :" , zero_numbers)


n = int(input("Enter a number :"))
finder(n)