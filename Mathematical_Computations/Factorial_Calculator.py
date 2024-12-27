# Practice 30 | Factorial Calculator

try:
    # Prompt the user to enter a non-negative integer
    number = int(input("Enter a non-negative integer to calculate its factorial: "))
    
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
except ValueError as e:
    # Handle invalid input
    print(f"Invalid input: {e}")
    # Exit the program since 'number' is not defined
    exit()

# Initialize factorial result
answer = 1

# Calculate factorial using a for loop
for i in range(1, number + 1):
    answer *= i
    
# Display the factorial result
print(f"The factorial of {number} is {answer}")
