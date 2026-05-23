def input_temperature(temp_str):
    try:
        temp = int(temp_str)
        return temp
    except ValueError as a:
        print(f"Caught input_temperature error: {a}")
        return None


def test_temperature():
    print("=== Garden Temperature ===")
    temp_str = "25"
    print(f"\nInput data is '{temp_str}'")
    temp = input_temperature(temp_str)
    if temp is not None:
        print(f"Temperature is now '{temp}'°C")
    temp_str = "abc"
    print(f"\nInput data is '{temp_str}'")
    temp = input_temperature(temp_str)
    if temp is not None:
        print(f"Temperature is now '{temp}'°C")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
