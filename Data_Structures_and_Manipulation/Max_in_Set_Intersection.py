# Practice 38 | Find Maximum Number in Set Intersection

def get_set_input(prompt):
    """
    Prompt the user to enter a space-separated list of integers and return it as a set.
    
    Args:
        prompt (str): The input prompt to display to the user.
    
    Returns:
        set: A set of integers entered by the user.
    """
    while True:
        try:
            user_input = input(prompt)
            # Convert input string to a set of integers
            return set(map(int, user_input.split()))
        except ValueError as e:
            # Handle invalid input
            print(f"Invalid input! Please enter a space-separated list of integers. (Error: {e})")

def main():
    """
    Find the intersection of two sets entered by the user and print the maximum element.
    """
    # Get sets A and B from the user
    set_A = get_set_input("Enter elements for set A (space-separated integers): ")
    set_B = get_set_input("Enter elements for set B (space-separated integers): ")

    # Find the intersection of set A and set B
    intersection_set = set_A.intersection(set_B)

    # Check if the intersection set is not empty
    if intersection_set:
        # Find and display the maximum element in the intersection
        print("The maximum element in the intersection is:", max(intersection_set))
    else:
        # Inform the user if there are no common elements
        print("No common elements between the sets.")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
