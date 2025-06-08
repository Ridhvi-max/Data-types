print("Decimal to Binary Converter")

n = int(input("How many numbers to convert? "))
count = 0

while count < n:
    decimal = int(input(f"Enter decimal number {count + 1}: "))
    binary = []

    while decimal > 0:
        remainder = decimal % 2              # Calculate remainder (0 or 1)
        binary.append(str(remainder))       # Convert remainder to string and add to list
        decimal = decimal // 2

    if not binary:                          # If list is empty (meaning input was 0)
        binary.append('0')

    binary.reverse()                       # Reverse list to get correct binary order
    print("Binary:", ''.join(binary))     # Join list elements to form string output

    count += 1