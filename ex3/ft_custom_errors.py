class GardenError (Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def default_error(self):
        if self.message == None:
            print("Unknown plant error")
# class PlantError (GardenError):

# class WaterError (GardenError):

def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    # try:
    #     raise PlantError("The plant is wilting!")
    # except PlantError as e:
    #     print(f"Caught PlantError: {e.message}")
    # try:
    #     raise WaterError("The water is contaminated!")
    # except WaterError as e:
    #     print(f"Caught WaterError: {e.message}")
    try:
        raise GardenError(None)
    except GardenError as e:
        print("\nCaught GardenError with no message:")
        e.default_error()
    print("\nAll custom error types work correctly!")

if __name__ == "__main__":
    test_custom_errors()