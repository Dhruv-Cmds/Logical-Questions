# Author: Dhruv

# Takes a password as input.
# Checks if the password length is at least 8 characters.
# Checks whether the password contains:
# At least one letter
# At least one digit
# Returns "Strong" if both conditions are satisfied.
# Otherwise, returns "Weak".
# Prints the result.

def check_strength(pwd):
    has_digit = False
    has_letter = False

    if len(pwd) < 8:
        return "Weak"
    
    for i in pwd:
        if i.isdigit():
            has_digit = True
        elif i.isalpha():
            has_letter = True

    if has_digit and has_letter:
        return "Strong"
    else:
        return "Weak"

pwd = input ("Enter password :")
print(check_strength(pwd))