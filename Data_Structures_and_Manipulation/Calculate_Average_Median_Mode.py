# Practice 55 | Calculate Average, Median, and Mode

try:
    # Prompt the user to enter a list of integers separated by spaces
    user_input = input("Enter numbers separated by spaces: ")
    user_list = list(map(int, user_input.split()))
    
    if len(user_list) == 0:
        raise ValueError("The list of numbers is empty.")
    
    # Calculate average
    average_numbers = sum(user_list) / len(user_list)
    
    # Sort the list to calculate median
    sorted_list = sorted(user_list)
    n = len(sorted_list)
    
    # Calculate median
    if n % 2 != 0:
        median = sorted_list[n // 2]
    else:
        median1 = sorted_list[n // 2]
        median2 = sorted_list[n // 2 - 1]
        median = (median1 + median2) / 2
    
    # Calculate frequency of each number for mode
    frequency = {}
    for item in user_list:
        frequency[item] = frequency.get(item, 0) + 1
    
    # Find the highest frequency
    max_count = max(frequency.values())
    
    # Find all numbers with the highest frequency
    modes = [key for key, count in frequency.items() if count == max_count]
    
    # Display the results
    print(f"Average: {average_numbers}")
    print(f"Median: {median}")
    print(f"Mode(s): {modes}")

except ValueError as e:
    # Handle invalid input
    print(f"Error: {e}")
