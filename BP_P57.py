# Python Program

# User Define Exception

class InvalidAgeException(Exception):
    "This Raised when the input value is less than 18(age)."
    pass

age = 18

try:
    num = int(input("Enter a Integer value: "))
    if num < age:
        raise InvalidAgeException
    else:
        print("Eligible to Vote.")

except InvalidAgeException:
    print("Exception Occurred: Invalid Age.")

# Thanks For Watching
