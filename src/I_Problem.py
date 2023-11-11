def smallest_factors(n):
    factors = []
    i = 2  # Start with the smallest prime number
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors

def main():
    num = int(input("Enter an integer: "))
    
    if num <= 1:
        print("The input must be greater than 1.")
    else:
        factors = smallest_factors(num)
        print("Smallest factors in increasing order:", ", ".join(map(str, factors)))

if __name__ == "__main__":
    main()
