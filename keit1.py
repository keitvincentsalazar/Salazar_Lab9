rows = int(input("Enter the number of rows: "))  # 1. Initialization

# 2. Outer Loop
for i in range(1, rows + 1):
    # 3. Print Spaces
    for space in range(rows - i):
        print(" ", end="")  # Print spaces for alignment
    
    # 4. Inner Loop (Print Asterisks)
    for star in range(2 * i - 1):
        print("*", end="")  # Print asterisks
    
    print()