import random
options=["Rock","Paper","Scissor"]
user_choice=input("Enter rock paper scissor: ")
print("You: ",user_choice)
computer_choice=random.choice(options)
print("Computer:",computer_choice)
if user_choice==computer_choice:
    print("it is a tie")
elif user_choice=="Rock" and computer_choice=="Scissor":
    print("You win!")
elif user_choice=="Paper" and computer_choice=="Rock":
    print("You win!")
elif user_choice=="Scissor" and computer_choice=="Paper":
    print("You win!")
else:
    print("You lose.")
