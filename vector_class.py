# Author: Dhruv

# Vector Class Challenge
# Create a vector class of 3 dimensions:
# overload + for addition
# overload * for dot product
# override __str__() to print like:
# 2i + 3j + 4k

class vector:
    
    def __init__(self , x , y , z):

        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return vector(self.x + other.x , self.y + other.y , self.z + other.z)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __str__(self):
        return f"{self.x} , {self.y} , {self.z}"
    

v1 = vector(1 , 2 , 3)
v2 = vector(4 , 5 , 6)
v3 = vector(7 , 8 , 9)

# ADD combinations
print("Addition is :" ,v1 + v2)
print("Addition is :" ,v2 + v3)
print("Addition is :" ,v1 + v3)

# MUL (dot product) combinations
print("Multiplecation is :" ,v1 * v2)
print("Multiplecation is :" ,v2 * v3)
print("Multiplecation is :" ,v1 * v3)
