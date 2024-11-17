# math_operations.py
# Created by: Anna Knowles

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    if b == 0:      #Rather than throwing an exception, if program is divided by 0, it will return a nice message
        return "Cannot divide by 0"
    return a / b  # Potential division by zero error

def multiply_numbers(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)                       #calls and tests divide_numbers function
    print(f"The result of division is: {result}")

    productResult = multiply_numbers(x, y)              #calls and tests multiply_numbers function
    print(f"The result of multiplication is: {productResult}")
