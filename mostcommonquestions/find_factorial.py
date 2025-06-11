def find_factorial(input_number):
    if input_number == 0:
        return 1
    else:
        return input_number * find_factorial(input_number - 1)

number = 5
result = find_factorial(number)
print(f"The factorial of {number} is {result}")