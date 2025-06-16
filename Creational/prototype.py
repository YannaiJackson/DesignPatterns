import copy


# Prototype base class
class Prototype:
    def clone(self):
        return copy.deepcopy(self)


# Concrete class
class Car(Prototype):
    def __init__(self, brand, model, options):
        self.brand = brand
        self.model = model
        self.options = options

    def __str__(self):
        return f"{self.brand} {self.model}, options: {self.options}"


# Usage
if __name__ == "__main__":
    original_car = Car(
        brand="Toyota",
        model="Corolla",
        options={"color": "red", "sunroof": True}
    )
    print("Original:", original_car)

    cloned_car = original_car.clone()
    cloned_car.options["color"] = "blue"
    print("Cloned:  ", cloned_car)
    print("Original after clone modified:", original_car)
