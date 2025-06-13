try:
    num=int(input("Write a number"))
    print(num)
except ValueError as ex:
    print("Exception:", ex)