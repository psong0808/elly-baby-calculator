def calculate(expression):
    try:
        # Evaluate the expression directly using eval
        result = eval(expression)
        return int(result)  # Ensure the result is an integer
    except Exception as e:
        print(f'Error evaluating expression: {expression}. Error: {str(e)}')
        return None

# Example usage (this line would be outside the function in actual use):
# print(calculate('14 - 5'))  # Output: 9