# mypy will display an error for the faulty code that raises the
# TypeError. That’s its job! So, to test this exception, we need
# to keep this error on purpose.
def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file").read()
    elif operation_number == 3:
        "Plant" + 42
    else:
        print("Operation completed successfully")
        return


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    print("Testing operation 4...")
    try:
        garden_operations(4)
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
