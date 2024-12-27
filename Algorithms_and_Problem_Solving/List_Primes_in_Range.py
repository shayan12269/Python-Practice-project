# Practice 57 | List Prime Numbers in Range

import math  # Used for square root calculation

try:
    # Get the start and end of the range from the user
    user_start_range = int(input("Start range: "))
    user_end_range = int(input("End range: "))
    
    # Initialize an empty list to store prime numbers
    prime_list = []
    
    # Iterate through the range to find prime numbers
    for prime in range(user_start_range, user_end_range + 1):
        if prime <= 1:
            # Numbers less than or equal to 1 are not prime
            continue
        else:
            is_prime = True
            # Check for factors up to the square root of the number
            for i in range(2, int(math.sqrt(prime)) + 1):
                if prime % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_list.append(prime)
    
    # Display the list of prime numbers found
    print(f"The prime numbers between {user_start_range} and {user_end_range} are {prime_list}")

except ValueError as e:
    # Handle invalid input
    print(f"Invalid input: {e}")
