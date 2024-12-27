# Practice 23 | Safe Division with Error Handling

while True:
    try:
        # Prompt the user to enter an integer
        number = int(input("Enter an integer to divide 1 by it: "))
        break  # Exit the loop if input is valid
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a valid integer.")

try:
    # Attempt to divide 1 by the entered number
    result = 1 / number
    print(f"Result of 1 divided by {number} is {result}")
except ZeroDivisionError:
    # Handle division by zero
    print("Error: Division by zero is not allowed.")
