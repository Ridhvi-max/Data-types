def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
my_tuple = (2, 3, 5, 7)
result = calculate_product(my_tuple)
print("The product of all numbers in the tuple is:", result)