class GardenError (Exception):
    def __init__(self, message="Unknown garden error"):
        self.message = message
        super().__init__(self.message)


class PlantError (GardenError):
    def __init__(self, message="Unknown plant error"):
        self.message = message
        super().__init__(self.message)


class WaterError (GardenError):
    def __init__(self, message="Unknown water error"):
        self.message = message
        super().__init__(self.message)


def check_plant_health(plant_name, status):
    if status == "wilting":
        raise PlantError(f"The {plant_name} plant is wilting!")
    elif status == "diseased":
        raise PlantError(f"The {plant_name} plant is diseased!")


def check_water(water, required_water):
    if water < required_water:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        check_plant_health("tomato", "wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e.message}")
    print("\nTesting WaterError...")
    try:
        check_water(5, 10)
    except WaterError as e:
        print(f"Caught WaterError: {e.message}")
    print("\nTesting catching all garden errors...")
    try:
        check_plant_health("tomato", "wilting")
    except GardenError as e:
        print(f"Caught GardenError: {e.message}")
    try:
        check_water(5, 10)
    except GardenError as e:
        print(f"Caught GardenError: {e.message}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
