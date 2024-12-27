# Practice 31 | Create Lists of Odd and Even Numbers

try:
    # Prompt the user to enter a positive integer
    user_number = int(input("Enter a positive integer: "))
    
    if user_number <= 0:
        raise ValueError("Please enter a number greater than zero.")

except ValueError as e:
    # Handle invalid input
    print(f"Invalid input: {e}")
    # Exit the program since 'user_number' is not defined
    exit()

# Initialize an empty list to store numbers
number_list = []

# Generate a list of numbers from 1 to user_number
for i in range(user_number):
    i += 1
    number_list.append(i)

# Separate even numbers
even_list = []
for even in number_list:
    if even % 2 == 0:
        even_list.append(even)
       
# Separate odd numbers
odd_list = []
for odd in number_list:
    if odd % 2 != 0:
        odd_list.append(odd) 
        
# Calculate sums
even_sum = sum(even_list)
odd_sum = sum(odd_list)

# Display the lists and their sums
print(f"List of even numbers: {even_list} with sum {even_sum}")
print(f"List of odd numbers: {odd_list} with sum {odd_sum}")
