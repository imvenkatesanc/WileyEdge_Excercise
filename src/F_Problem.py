def main():
    # Get the Richter magnitude value from the user
    richter = float(input("Enter the Richter magnitude value: "))

    # Determine the level of damage based on the Richter magnitude
    if richter < 1.0:
        result = "Microearthquakes not felt or rarely felt"
    elif richter < 2.0:
        result = "Very rarely causes damage"
    elif richter < 4.0:
        result = "Damage done to weak buildings"
    elif richter < 5.0:
        result = "Cause damage to poorly constructed buildings"
    elif richter < 6.0:
        result = "Causes damage to well-built structures"
    elif richter < 7.0:
        result = "Causes damage to most buildings"
    elif richter < 8.0:
        result = "Causes major destruction"
    else:
        result = "Causes unbelievable damage"

    # Display the result
    print(f"Richter magnitude {richter} - {result}")

if __name__ == "__main__":
    main()
