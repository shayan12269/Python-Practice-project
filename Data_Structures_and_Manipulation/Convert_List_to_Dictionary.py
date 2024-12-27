# Practice 29 | Convert List to Dictionary

# Prompt the user to enter key-value pairs separated by commas
user_response = input("Enter key-value pairs in the format key1:value1, key2:value2, ...: ")

# Split the input string into individual pairs
pairs = user_response.split(',')

# Initialize an empty dictionary to store the key-value pairs
user_dict = {}

# Iterate through each pair to process and add to the dictionary
for pair in pairs:
    # Remove any leading/trailing whitespace from the pair
    pair = pair.strip()
    
    # Split the pair into key and value using ':' as the delimiter
    key_value = pair.split(':')
    
    # Check if the pair contains exactly one ':' to separate key and value
    if len(key_value) == 2:
        key = key_value[0].strip()
        value = key_value[1].strip()
        user_dict[key] = value
    else:
        # Inform the user about the incorrect format
        print(f"Invalid input format for '{pair}'. Please use key:value format.")

# Display the resulting dictionary
print("Resulting Dictionary:", user_dict)
