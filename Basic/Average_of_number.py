# Practice 8 | Compute Average of Numbers

try:
    # Prompt the user to input numbers separated by spaces
    input_number = input("Average of numbers: ")
    
    # Split the input string into individual number strings, strip any whitespace, and convert to float
    number_list = [float(num.strip()) for num in input_number.split() if num.strip()]
    
    # Check if the list is empty
    if len(number_list) == 0:
        raise ValueError("You have to write a number!")
    
    # Calculate the average
    average = sum(number_list) / len(number_list)
    
    # Print the result with two decimal places
    print(f"Average of the {number_list} is: {average:.2f}")
    
except ValueError as e:
    print(f"Error: {e}") 

