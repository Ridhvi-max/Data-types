import random
playing=True
number=str(random.randint(10,20))
print("I will generate a number from 10 to 20, and you have to guess the number one gigit at a time.")
print("the game ends when you got 1 hero!")
while playing:
    guess=input("Give me your best guess! \n")
    if number==guess:
        print("You win the game")
        print("the number was",number)
        break
    else:
        print("Your guess isn't quite right, try again \n")