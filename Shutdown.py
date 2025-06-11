def shutdown(command="Yes"):
    """
    Checks the user's input and returns the shutdown status.
    """
    if command.lower() == "yes":
        print("Shutting down...")
    elif command.lower() == "no":
        print("Shutdown aborted.")
    else:
        print("Sorry. Invalid input. Try again.")
        new_input = input("Do you want to shutdown the system? (Yes/No): ")
        shutdown(new_input)  # recursion (retry)
        

# Program starts here
user_input = input("Do you want to shutdown the system? (Yes/No): ")
shutdown(user_input)