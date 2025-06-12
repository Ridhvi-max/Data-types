def calculate_due(bill, paid):
    return bill - paid

while True:
    name = input("Enter your name (or type 'exit' to quit): ")
    if name == 'exit':
        break

    bill = float(input("Enter total bill: "))
    paid = float(input("Enter amount paid: "))

    due = calculate_due(bill, paid)
    print("Hello", name + ", your due amount is ₹", due)