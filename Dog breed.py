class Dog:
    # Class variable
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed


# Create two Dog objects of different breeds
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Beagle")

# Print dog details
print("Dog 1 Details:")
print("Name:", dog1.name)
print("Breed:", dog1.breed)
print("Species:", Dog.species)

print()

print("Dog 2 Details:")
print("Name:", dog2.name)
print("Breed:", dog2.breed)
print("Species:", Dog.species)
