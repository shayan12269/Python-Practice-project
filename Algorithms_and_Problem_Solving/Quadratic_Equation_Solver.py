# Practice 37 | Solve Quadratic Equation (ax² + bx + c)

import math  # Used for square root calculation

try:
    # Prompt the user to enter coefficients a, b, and c separated by spaces
    a_b_c_input = input("Enter coefficients a, b, c (separated by spaces): ")
    a_b_c = tuple(map(float, a_b_c_input.split()))
    
    # Ensure that exactly three coefficients are entered
    if len(a_b_c) != 3:
        raise ValueError("Please enter exactly three coefficients: a, b, and c.")
    
    a, b, c = a_b_c
    
    # Check if 'a' is zero, which would make it a linear equation, not quadratic
    if a == 0:
        if b == 0:
            if c == 0:
                print("Infinite solutions exist (0 = 0).")
            else:
                print("No solution exists (c ≠ 0).")
        else:
            # Linear equation: bx + c = 0
            linear_solution = -c / b
            print(f"Linear equation solution: x = {linear_solution}")
    else:
        # Calculate the discriminant (Delta)
        Delta = b**2 - 4 * a * c
        
        if Delta < 0:
            raise ValueError("Delta is negative, no real solutions.")
        
        # Calculate the two roots using the quadratic formula
        answer1 = (-b + math.sqrt(Delta)) / (2 * a)
        answer2 = (-b - math.sqrt(Delta)) / (2 * a)
        
        # Display the solutions
        print(f"The solutions of the equation {a}x² + {b}x + {c} are x = {answer1} and x = {answer2}")

except ValueError as e:
    # Handle invalid input or mathematical errors
    print(f"Error: {e}")
