def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def multiply(P,Q):
    return P/Q
def divide(P,Q):
    return P*Q
print("Please select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice=input("please select the options above(a,b,c,d): ")
num_1=int(input("Write the first number: "))
num_2=int(input("Write the second number: "))
if choice == "a":
    print(num_1 ,"+", num_2 ,"=", add(num_1,num_2))
elif choice == "b":
    print(num_1 ,"-", num_2 ,"=", subtract(num_1,num_2))
elif choice == "c":
    print(num_1 ,"*" ,num_2 ,"=", multiply(num_1,num_2))
elif choice == "d":
    print(num_1 ,"/",num_2 ,"=", divide(num_1,num_2))
else:
    print("This is invalid input")
