# Practice 56 | Highest Difference Between Consecutive Numbers

try:
    # Prompt the user to enter a list of integers separated by spaces
    user_input = input("Enter a list of integers separated by spaces: ")
    user_list = list(map(int, user_input.split()))
    
    # Check if the list has at least two elements
    if len(user_list) < 2:
        print("Error: Please enter at least two integers.")
    else:
        # Sort the list in ascending order
        user_sorted_list = sorted(user_list)
        
        # Calculate differences between consecutive numbers
        differ_list = [user_sorted_list[i + 1] - user_sorted_list[i] for i in range(len(user_sorted_list) - 1)]
        
        # Find the highest difference
        highest_diff = max(differ_list)
        
        # Display the highest difference
        print(f"Highest Difference: {highest_diff}")

except ValueError:
    # Handle invalid input
    print("Error: Please enter only integers separated by spaces.")
