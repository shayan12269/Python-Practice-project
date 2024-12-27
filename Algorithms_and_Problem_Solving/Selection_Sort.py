# Practice 49 | Selection Sort Implementation

while True:
    # Prompt the user to enter elements separated by spaces
    user_input = input("Enter elements to sort (or type 'break' to quit): ").split()
    
    # Prompt the user to choose sorting order
    user_sorted_selection = input("Sort by 'ascending' or 'descending' (type 'break' to quit): ").lower()
    
    # Separate numbers and non-digit characters
    user_numbers = [int(num) for num in user_input if num.isdigit()]  
    user_letters = [letter for letter in user_input if not letter.isdigit()]  
    
    # Exit the loop if the user types 'break'
    if user_sorted_selection == 'break': 
        print("Exiting the sorting program.")
        break
    
    elif user_sorted_selection == 'ascending':  
        # Sort numbers in ascending order and concatenate with sorted letters
        ascending_sorted = sorted(user_numbers) + sorted(user_letters)
        print("Sorted List (Ascending):", ascending_sorted)
        
    elif user_sorted_selection == 'descending':  
        # Sort numbers in descending order and concatenate with sorted letters
        descending_sorted = sorted(user_numbers, reverse=True) + sorted(user_letters, reverse=True)
        print("Sorted List (Descending):", descending_sorted)
    
    else:
        # Handle invalid sorting option
        print("Invalid sorting option. Please choose 'ascending' or 'descending'.")
