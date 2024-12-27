Input_number = input("Average of numbers: ")

try:
    number_list = [float(num.strip()) for num in Input_number.split() if num.strip()]
    if len(number_list) == 0:
        raise ValueError("You have to write a number!")

    count = len(number_list)
    Average = sum(number_list)/count
    
    print(f"Average of the {number_list} is: {Average:.2f}")
    
except ValueError as e:
    print(f"Erore:{e}") 
