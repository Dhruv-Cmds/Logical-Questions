# Author: Dhruv

# Create class Student:
# Attributes:
# name
# marks (out of 100)
# Method:
# '''get_grade()
# Grade rules:'''
# Marks	Grade
# ≥ 90	A
# ≥ 75	B
# ≥ 60	C
# ≥ 40	D
# < 40	F
# Print name + grade.

class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def result (self):

        if (self.marks < 0 or self.marks > 100):
            print ("Invalid marks")
            return

        elif (self.marks >= 90):
            grade = 'A'
            
        elif (self.marks >= 75):
            grade = 'B'

        elif (self.marks >= 60):
            grade = 'C'

        elif (self.marks >= 40):
            grade = "D"
        
        else:
            grade = 'F'

        print(f"{self.name}'s Grade is: {grade}")

marks = int(input("Enter marks: "))
s1 = Student("Dhruv", marks)
s1.result()