# Practice 41 | Recursive Square Root Finder

# Define a recursive function to calculate square root
def square_root_recursive(n, guess=1.0):
    """
    Calculate the square root of a number using recursion (Newton-Raphson method).
    
    Args:
        n (float): The number to find the square root of.
        guess (float): The current guess for the square root.
    
    Returns:
        float: The approximated square root of n.
    """
    # Check if the current guess is close enough to the actual square root
    if abs(guess ** 2 - n) < 0.00001:
        return guess
    else: 
        # Update the guess using Newton-Raphson formula
        new_guess = (guess + n / guess) / 2
        return square_root_recursive(n, new_guess)

try:
    # Prompt the user to enter a number
    user_number = float(input("Enter a number to find its square root: "))
    
    if user_number < 0:
        print("Error: Cannot compute the square root of a negative number.")
    else:
        # Calculate the square root
        sqrt_result = square_root_recursive(user_number)
        # Display the result rounded to two decimal places
        print(f"The square root of {user_number} is approximately {sqrt_result:.2f}")

except ValueError:
    # Handle invalid input
    print("Invalid input. Please enter a valid number.")
