class Bus:
    def __init__(self):
        self.fare = int(input("Enter fare per passenger: "))
        self.passengers = int(input("Enter number of passengers: "))

    def total_fee(self):
        return self.fare * self.passengers
bus1 = Bus()
print("Total fee:", bus1.total_fee())