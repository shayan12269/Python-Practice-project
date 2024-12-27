# Practice 36 | Find Maximum Value in a 2D Matrix

try:
    # Prompt the user to enter elements for a 2x2 matrix
    a = int(input("Enter element at row 1, column 1: "))
    b = int(input("Enter element at row 1, column 2: "))
    c = int(input("Enter element at row 2, column 1: "))
    d = int(input("Enter element at row 2, column 2: "))
    
    # Create the 2x2 matrix as a list of lists
    matrix_list = [
        [a, b],
        [c, d]
    ]
    
    # Find the maximum value in each row and then find the overall maximum
    max_value = max(max(row) for row in matrix_list)
    
    # Display the maximum value
    print(f"The largest number in the matrix is: {max_value}")

except ValueError:
    # Handle invalid input
    print("Invalid input. Please enter integer values for the matrix elements.")
