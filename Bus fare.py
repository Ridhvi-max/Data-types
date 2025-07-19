class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100  # Default fare: ₹100 per passenger


class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10  # 10% extra charge
        total_fare = base_fare + maintenance_charge
        return total_fare


# Example usage
school_bus = Bus("School Volvo", 12, 50)
print("Vehicle Name:", school_bus.name)
print("Total Bus Fare:", school_bus.fare())