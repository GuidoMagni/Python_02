class GardenError (Exception):
    def __init__(self, message="Unknown garden error"):
        self.message = message
        super().__init__(self.message)


class PlantError (GardenError):
    def __init__(self, message="Unknown plant error"):
        self.message = message
        super().__init__(self.message)


def water_plant(plant_name):
    if not plant_name[0].isupper():
        raise PlantError(
                        f"Invalid plant name to water: '{plant_name}'\n"
                        ".. ending tests and returning to main"
                        )
    print(f"Watering {plant_name}: [OK]")


def test_watering_system():
    print(
        "=== Garden Watering System ===\n"
        "\nTesting valid plants...\n"
        "Opening watering system"
        )
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system\n")
    print(
        "Testing invalid plants...\n"
        "Opening watering system"
        )
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print(
            "Closing watering system\n"
            "\nCleanup always happens, even with errors!"
            )


if __name__ == "__main__":
    test_watering_system()
