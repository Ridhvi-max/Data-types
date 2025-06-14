
import math
print("Welcome to Trignometry calculator")
Angles=str(input("What do you want to calculate: "))
user_input=float(input("Write the value: "))
if Angles=="sine":
    print(math.sin(user_input))
elif Angles=="cosine":
    print(math.cos(user_input))
elif Angles=="tangent":
    print(math.tan(45))
else:
    print("Write the valid user_input")