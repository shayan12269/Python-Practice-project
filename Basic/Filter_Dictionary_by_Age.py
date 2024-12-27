# Practice 28 | Filter Dictionary by Age

# Define a dictionary with people's names and their ages
people_ages = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 28,
    "David": 35,
    "Eva": 22,
    "Frank": 40,
    "Grace": 29,
    "Hannah": 33,
    "Ivy": 27,
    "Jack": 31,
    "Karen": 26,
    "Leo": 34,
    "Mia": 24,
    "Noah": 32,
    "Olivia": 36,
    "Paul": 38,
    "Quincy": 23,
    "Rachel": 29,
    "Steve": 41,
    "Tina": 39,
    "Uma": 28,
    "Victor": 33,
    "Wendy": 30,
    "Xander": 25,
    "Yara": 37,
    "Zach": 26,
    "Amelia": 32,
    "Brian": 34,
    "Chloe": 22
}

try:
    # Prompt the user to enter an age threshold
    age_threshold_input = input("Enter an age to filter names with age below this value: ")
    age_threshold = int(age_threshold_input)
    
    # Create a list of names where age is less than the specified threshold
    less_than_threshold = [name for name, age in people_ages.items() if age < age_threshold]
    
    # Display the filtered list of names
    print(f"People with age less than {age_threshold}: {less_than_threshold}")

except ValueError:
    # Handle invalid input
    print("Invalid input. Please enter a valid integer for age.")
