def firstDigit(n):
    while n >= 10:
        n //= 10
    return n

def lastDigit(n):
    return n % 10

def digits(n):
    return len(str(n))

def main():
    n = int(input("Enter an integer: "))
    
    first = firstDigit(n)
    last = lastDigit(n)
    num_digits = digits(n)
    
    print(f"First digit: {first}")
    print(f"Last digit: {last}")
    print(f"Number of digits: {num_digits}")

if __name__ == "__main__":
    main()
