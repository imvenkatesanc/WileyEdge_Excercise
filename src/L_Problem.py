def allTheSame(x, y, z):
    return x == y == z

def allDifferent(x, y, z):
    return x != y and y != z and x != z

def sorted(x, y, z):
    return x <= y <= z

def main():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    z = int(input("Enter the third number: "))
    
    print(f"All the same: {allTheSame(x, y, z)}")
    print(f"All different: {allDifferent(x, y, z)}")
    print(f"Sorted: {sorted(x, y, z)}")

if __name__ == "__main__":
    main()
