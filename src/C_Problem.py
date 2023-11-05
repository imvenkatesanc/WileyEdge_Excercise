# a. One birth every 7 seconds
# b. One death every 13 seconds
# c. One new immigrant every 45 seconds Write a program to to prompt the user to enter the number of years and displays the population after the number of years. The population should be cast into an integer. Here is a sample run of the program: Enter the number of years: 5 The population in 5 years is 325932970

year = int(input("Enter the number of years: "))

#seconds per time
seconds_per_year = 365*24*60*60

#user input conversion
convert_to_sec = seconds_per_year*year

#birth calculation
birth = convert_to_sec // 7

#death calculation
death = convert_to_sec // 13

#immigrant calculation
immigrant = convert_to_sec // 45

#finally
population = birth + death - immigrant

print(f"The population in {year} years is: {population}")