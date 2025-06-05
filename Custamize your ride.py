print("Select your ridd: ")
print("1. Bike")
print("2. Car")
choice=int(input("Enter your choice: "))
if(choice==1):
    print("what type of bike? ")
    print("1.Scooty\n")
    print("2.Scooty\n")
    choice2=int(input("Enter your choiec2: "))
    if choice2==1:
        print("You have selected scooter")
    else:
        print("you have selected scotter")
elif(choice==2):
    print("what type of car?")
    print("1.Sedan")
    print("2.XUV")
    choice3=int(input("enter your choice3: ")) 
    if choice3==1:
        print("you have selected XUV") 
    else:
        print("you have selected XUV")
else:
    print("Wrong choice!")

