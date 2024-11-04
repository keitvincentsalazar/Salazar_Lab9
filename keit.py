rows = int(input("Enter the number of rows: "))  # Prompt user for the number of rows

# Loop in each row
for i in range(1, rows + 1):
    # Print spaces to center the pyramid
    for space in range(rows - i):
        print(" ", end="")  # Print spaces for alignment
    
    # Print asterisks for the current row
    for star in range(2 * i - 1):
        print("*", end="")  # Print asterisks
    # Move to the next line after print a row
    print()
