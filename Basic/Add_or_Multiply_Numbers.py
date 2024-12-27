# Practice 13 | Add or Multiply Numbers

from functools import reduce

while True: 
    # Prompt the user to choose an operation
    operation = input("Choose operation - Add or Multiply (or type 'exit' to quit): ").lower()
    
    if operation == 'exit':
        print("Exiting the Add or Multiply program.")
        break
    
    # Prompt the user to enter numbers separated by spaces
    input_numbers = input("Enter numbers separated by spaces: ")
    
    try:
        # Convert the input string to a list of integers
        number_list = [int(num.strip()) for num in input_numbers.split() if num.strip()]
        
        if len(number_list) == 0:
            raise ValueError("No numbers were entered!")
        
        if operation == 'add':
            # Calculate the sum of the numbers
            total_number = sum(number_list)
            print(f"Total: {total_number}")
            
        elif operation == 'multiply':
            # Calculate the product of the numbers
            multiply_number = 1
            for num in number_list:
                multiply_number *= num
            print(f"Product: {multiply_number}")
        
        else:
            # Handle invalid operation input
            print("Invalid operation. Please choose 'add' or 'multiply'.") 
            continue
        
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
