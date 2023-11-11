def print_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n, i, -1):
            print("   ", end="")
        
        # Print decreasing numbers
        for j in range(i, 1, -1):
            print(f"{j:2d} ", end="")
        
        # Print increasing numbers
        for j in range(2, i + 1):
            print(f"{j:2d} ", end="")
        
        print()  # Move to the next line

def main():
    n = int(input("Enter the number of lines (1-15): "))
    
    if 1 <= n <= 15:
        print_pyramid(n)
    else:
        print("Please enter a number between 1 and 15.")

if __name__ == "__main__":
    main()
