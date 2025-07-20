size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop to print stars in a row
    for col in range(size):
        print("*", end="")  # Stay on the same line
    print()  # Move to the next line after each row
    row += 15
    
