# Practice 53 | Plot Points on a Grid

try:
    # Get the number of points from the user
    user_point_number = int(input("Number of points: "))
    
    number_point = 1
    points = []
    
    # Collect each point's coordinates from the user
    while number_point <= user_point_number: 
        user_input = input(f"Point {number_point} - Enter x, y (separated by comma): ")
        try:
            x, y = map(int, user_input.split(","))
            points.append((x, y))
            number_point += 1
        except ValueError:
            print("Invalid input. Please enter numbers in 'x,y' format.")
    
    print("Collected Points:", points)
    
    # Determine the size of the grid
    if points:
        max_x = max(point[0] for point in points) + 1
        max_y = max(point[1] for point in points) + 1
    else:
        max_x, max_y = 0, 0
    
    # Check if grid size is too large
    if max_x > 20 or max_y > 20:
        user_answer = input("The grid size is large. Please use smaller numbers (press '+' to continue): ")
        if user_answer != "+":
            print("Exiting the program.")
            exit()
    
    # Display the grid representation
    print("\nGrid Representation:")
    for y in range(max_y, -1, -1): 
        row = ""
        for x in range(max_x + 1): 
            if (x, y) in points:
                row += "● "  
            else:
                row += ". "  
        print(row)

except ValueError:
    print("Invalid input. Please enter a valid number of points.")
