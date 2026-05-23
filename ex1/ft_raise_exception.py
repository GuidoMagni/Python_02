def input_temperature(temp_str):
    try:
        temp = int(temp_str)
        if temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
        if temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
        return temp
    except ValueError as a:
        print(f"Caught input_temperature error: {a}")
        return None


def test_temperature():
    print("=== Garden Temperature Checker ===")
    temp_str = "25"
    print(f"\nInput data is '{temp_str}'")
    temp = input_temperature(temp_str)
    if temp is not None:
        print(f"Temperature is now {temp}°C")
    temp_str = "abc"
    print(f"\nInput data is '{temp_str}'")
    temp = input_temperature(temp_str)
    if temp is not None:
        print(f"Temperature is now {temp}°C")
    temp_str = "100"
    print(f"\nInput data is '{temp_str}'")
    temp = input_temperature(temp_str)
    if temp is not None:
        print(f"Temperature is now {temp}°C")
    temp_str = -50
    print(f"\nInput data is '{temp_str}'")
    temp = input_temperature(temp_str)
    if temp is not None:
        print(f"Temperature is now {temp}°C")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
