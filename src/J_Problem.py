def main():
    n = int(input("Enter the size of the multiplication table: "))
    
    # Print the header row
    print("   |", end="")
    for i in range(1, n + 1):
        print(f"{i:4d}", end="")
    print("\n" + "-" * (n * 5 + 6))
    
    # Generate and print the multiplication table
    for i in range(1, n + 1):
        print(f"{i:2d} |", end="")
        for j in range(1, n + 1):
            result = i * j
            print(f"{result:4d}", end="")
        print()

if __name__ == "__main__":
    main()
