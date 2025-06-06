number = int(input("Enter a number: "))
temp=number
count = 0
while temp > 0:
    temp = temp // 10  
    count += 1         

if number == 0:
    count = 1

print("Number of digits:", count)