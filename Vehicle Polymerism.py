class BMW:
    def start_engine(self):
        print("BMW engine started with a roar!")

    def speed(self):
        print("BMW can go up to 250 km/h.")

class Ferrari:
    def start_engine(self):
        print("Ferrari engine started with a thunderous sound!")

    def speed(self):
        print("Ferrari can go up to 340 km/h.")

# Polymorphism implementation
def car_test(car):
    car.start_engine()
    car.speed()

# Creating objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Using polymorphism
print("Testing BMW:")
car_test(bmw_car)

print("\nTesting Ferrari:")
car_test(ferrari_car)
