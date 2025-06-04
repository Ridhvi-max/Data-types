medical_cause = input("do you have a medical cause Y or N: ")
attendence=int(input("Enter the attendence of the student: "))
if medical_cause =="Y":
    print("You are allowed")
else:
    if attendence>=75:
        print("You are allowed")
    else:
        print("You are not allowed")