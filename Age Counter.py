print("Enter your age:")

age_input = input()  # Take input from user

try:
    age = int(age_input)  # Try converting input to integer
    if age % 2 == 0:
        print("The age is even.")
    else:
        print("The age is odd.")
except ValueError:
    print("ValueError: Please enter a valid integer for age.")