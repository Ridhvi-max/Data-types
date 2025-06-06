print("Welcome to Calculator!")
    
base = float(input("Enter the base number: "))
    
n = int(input("Enter how many powers you want to calculate: "))
for i in range(1, n + 1):
        exponent = float(input(f"Enter exponent #{i}: "))
        result = base ** exponent
        print(f"{base} ^ {exponent} = {result}")
