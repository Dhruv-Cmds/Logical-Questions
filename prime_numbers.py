# Author: Dhruv

# is_prime(n)
# Return:
# True if prime
# False otherwise
# Then use this function inside a loop from 1 to 50 and print all primes.
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range (2 , n):
       if n % i == 0:
         return False
    return True

for i in range (1 , 51):
     if is_prime(i):
        print(i)