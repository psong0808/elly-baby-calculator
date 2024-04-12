def main():
    print("Addition: 5 + 3 =", add(5, 3))
    print("Subtraction: 5 - 3 =", subtract(5, 3))
    print("Multiplication: 5 * 3 =", multiply(5, 3))
    print("Division: 5 / 3 =", divide(5, 3))
    print("Exponentiation: 2 ^ 3 =", power(2, 3))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def power(base, exponent):
    return base ** exponent

main()


# Example usage (this line would be outside the function in actual use):
# print(calculate('14 - 5'))  # Output: 9
