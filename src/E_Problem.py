def main():
    # Get the amount from the user as a float value
    amount = float(input("Enter an amount, for example, 11.56: "))

    # Convert the amount to cents for easier calculations
    cents = int(amount * 100)

    # Calculate the number of dollars, quarters, dimes, nickels, and pennies
    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    pennies = cents % 5

    # Display the result
    print(f"Your amount {amount:.2f} consists of")
    print(f"{dollars} dollars")
    print(f"{quarters} quarters")
    print(f"{dimes} dimes")
    print(f"{nickels} nickels")
    print(f"{pennies} pennies")

if __name__ == "__main__":
    main()
