
def divide(a, b):
    """Safely divides two numbers, handling division by zero."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    finally:
        print("Division attempt finished.")

# --- Test the function ---
print(f"Result: {divide(10, 2)}")
print("-" * 20)
print(f"Result: {divide(10, 0)}")
