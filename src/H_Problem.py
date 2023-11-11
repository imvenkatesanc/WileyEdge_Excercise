def decimal_to_hexadecimal_binary(decimal):
    # Convert to hexadecimal
    hexadecimal = hex(decimal).upper()

    # Convert to binary
    binary = bin(decimal)[2:]

    return hexadecimal, binary

def main():
    decimal_number = int(input("Enter a decimal number: "))
    
    hexadecimal, binary = decimal_to_hexadecimal_binary(decimal_number)
    
    print(f"Decimal: {decimal_number}")
    print(f"Hexadecimal: 0x{hexadecimal}")
    print(f"Binary: 0b{binary}")

if __name__ == "__main__":
    main()
