# Author: Dhruv

# # Takes a number n from user
# # Prints numbers from 1 to n
# But:
# if number divisible by 3 → print "Fizz"
# if divisible by 5 → print "Buzz"
# if divisible by both 3 and 5 → print "FizzBuzz"
# else print the number

n = int(input("Enter a number :"))

for i in range (1 , n + 1):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz") 

    elif ( i % 3 == 0):
        print("Fizz")

    elif (i % 5 == 0):
        print("Buzz")

    else :
        print(i)

                                    #  SECOUND METHOD

def divisiable (n):

    divisiable_by_3 = []
    divisiable_by_5 = []
    divisiable_by_3_and_5 = []
    divisiable_by_none = []

    for i in range ( 1 , n + 1):

        if (i % 3 == 0 and i % 5 == 0):
            print(f"FizzBuzz {i}")

            divisiable_by_3_and_5.append(i)
        
        elif (i % 3 == 0):
            print(f"Fizz {i}")

            divisiable_by_3.append(i)
        
        elif (i % 5 == 0):
            print(f"Buzz {i}")

            divisiable_by_5.append(i)

        else:
            print(i)

            divisiable_by_none.append(i)

    print("\nALL LIST :")
    print(f"divisiable by 3 and 5 :{divisiable_by_3_and_5}")
    print(f"divisiable by 3 :{divisiable_by_3}")
    print(f"divisiable by 5 : {divisiable_by_5}")
    print(f"divisiable by none : {divisiable_by_none}")

n = int(input("Enter a number :"))
divisiable(n)
        