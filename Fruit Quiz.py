class FruitQuiz:
    def quiz(self):
        while True:
            print("\nWhich fruit is yellow and curved?")
            print("a) Apple\nb) Banana\nc) Grapes\nd) Orange")
            answer = input("Enter your answer (a/b/c/d): ").lower()

            if answer == 'b':
                print("Correct! 🎉")
            else:
                print("Wrong! The correct answer is 'b) Banana'.")

            option = int(input("\nEnter 0 if you want to play again, otherwise enter 1 to exit: "))
            if option:
                break

print("Welcome to the Fruit Quiz!")
fq = FruitQuiz()
fq.quiz()