string=str(input("Enter your string: "))
string2=('')
for i in string:
    string2=i+string2
print("\nThe original string: ",string)
print("the string after reversed: ",string2)