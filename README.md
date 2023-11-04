# WileyEdge_Excercise
Programming excercise preparation by Wiley Edge

This repository contains a set of programming problems and their solutions. Each problem is described below:

## Problem 1:
**1. Write a program that reads a Celsius degree in a double value from the console, then converts it to Fahrenheit and displays the result. The formula for the conversion is as follows:**
- fahrenheit = (95) celsius + 32

## Problem 2:
**2. Write a program that prompts the user to enter the minutes, and displays the number of years, months, weeks and days for the minutes. For simplicity, assume a year has 365 days and month has 30 days.**
- Here is a sample run:
- Enter the number of minutes: 1000000000
- 1000000000 minutes is approximately 1902 years, 7 months, 0 weeks and 4 days.

## Problem 3:
**3. The U.S. Census Bureau projects population based on the following assumptions:**
- a. One birth every 7 seconds
- b. One death every 13 seconds
- c. One new immigrant every 45 seconds
Write a program to to prompt the user to enter the number of years and displays the population after the number of years. The population should be cast into an integer. Here is a sample run of the program:
Enter the number of years: 5 The population in 5 years is 325932970

## Problem 4:
**4. Guessing Birthdays: You can find out the date of the month when your friend was born by asking five questions. Each question asks whether the day is in one of the five sets of numbers.
The birthday is the sum of the first numbers in the sets where the day appears. For example, if the birthday is 19, it appears in Set1, Set2, and Set5. The first numbers in these three sets are 1, 2, and 16. Their sum is 19.**

Write a program to achieve this. Here is a sample run:

    Is your birthday in Set1?
    1357 9 11 13 15
    17 19 21 23
    25 27 29 31
    Enter N for No and Y for Yes: Y
    Is your birthday in Set2?
    2367
    10 11 14 15
    18 19 22 23
    26 27 30 31
    Enter N for No and Y for Yes: Y
    Is your birthday in Set3? 4 5 6 7
    12 13 14 15
    20 21 22 23
    28 29 30 31 
    Enter N for No and Y for Yes: N
    Is your birthday in Set4?
    8 9 10 11
    12 13 14 15
    24 25 26 27
    28 29 30 31
    Enter N for No and Y for Yes: N
    Is your birthday in Sets?
    16 17 18 19
    20 21 22 23
    24 25 26 27 28 29 30 31
    Enter N for No and Y for Yes: Y
    Your birthday is 19!

  ## problem 5:
  **5. Suppose you want to develop a program that changes a given amount of money into smaller monetary units. The program lets the user enter an amount as a double value representing a total in dollars and cents, and outputs a report listing the monetary equivalent in the maximum number of dollars, quarters, dimes, nickels, and pennies, in this order, to result in the minimum number of coins. Refer the converstion table below-**

    100 Cents=1 Dollar
    25 Cents=1 Quarter
    10 Cents=1 Dime
    5 Cents =1 Nickel
    1 Cents=1 Penny

Here is a sample run:

    Enter an amount, for example, 11.56: 11.56 Your amount 11.56 consists of
    11 dollars
    2 quarters
    O dimes
    1 nickels
    1 pennies

## Problem 6:
**6.Write a program to read the Richter magnitude value from the user and display the result for the following conditions using if...elif...else statement.**

Richter Magnitude       Information

> 1.0 and <2.0          Microearthquakes not felt or rarely felt

> 2.0 and < 4.0         Very rarely causes damage

> 4.0 and < 5.0         Damage done to weak buildings

> 5.0 and < 6.0         Cause damage to the poorly constructed building

> 6.0 and < 7.0         Causes damage to well-built structures

> 7.0 and <8.0          Causes damage to most buildings

> 8.0 and < 9.0         Causes major destruction

> 9.0                   Causes unbelievable damage

## Problem 7:
**7.Day of the week: Zeller's congruence is an algorithm developed by Christian Zeller to calculate the day of the week. The formula is**

h =(q+26(m + 1)/10 +k + k/4 +j/4 +5j) % 7

where,
- h is the day of the week (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday, 4: Wednesday, 5: Thursday, 6: Friday).
- q iş the day of the month.
- m is the month (3: March, 4: April, 12: December). January and February are counted as months 13 and 14 of the previous year.
- i is the century (i.e., year/ 100).
- k is the year of the century (i.e., year % 100).

Note that the division in the formula performs an integer division. Write a program that prompts the user to enter a year, month, and day of the month, and displays the name of the day of the week. Here are some sample runs:

  - Enter year: (e.g., 2012): 2015
  - Enter month: 1-12: 1
  - Enter the day of the month: 1-31: 25
  - Day of the week is Sunday

  - Enter year: (e.g., 2012): 2012
  - Enter month: 1-12: 5
  - Enter the day of the month: 1-31:12
  - Day of the week is Saturday
## Problem 8:
**8.Write a program to convert a decimal number to a hexadecimal number & binary number? For example, the decimal number 123 is 7B in hexadecimal.**

## Problem 9:
**9. Write a program that reads an integer and displays all its smallest factors in increasing order.**
- For example, 
- if the input integer is 120, 
- the output should be as follows: 2, 2, 2, 3, 5.

## Problem 10:
**10.Write a program that uses nested for loops to display a multiplication table, Note: alignments are important in the output. Multiplication Table**

## Problem 11:
**11. Write a program that prompts the user to enter an integer from 1 to 15 and displays a pyramid, as shown in the following sample run:**
Enter the number of lines: 7

                         1
                      2  1  2
                   3  2  1  2  3
                4  3  2  1  2  3  4
             5  4  3  2  1  2  3  4  5
          6  5  4  3  2  1  2  3  4  5  6
       7  6  5  4  3  2  1  2  3  4  5  6  7


## Problem 12:

**12.Write the following functions and provide a program to test them.**
- a. def allTheSame(x, y, z) (returning true if the arguments are all the same)
- b. def allDifferent (x, y, z) (returning true if the arguments are all different)
- c. def sorted(x, y, z) (returning true if the arguments are sorted, with the smallest one coming first)

## Problem 13:

**13.Write the following functions and provide a program to test them.**
- a. def firstDigit(n) (returning the first digit of the argument)
- b. def lastDigit(n) (returning the last digit of the argument)
- c. def digits (n) (returning the number of digits in the argument) 
- For example, firstDigit (1729) is 1, lastDigit (1729) is 9, and digits (1729) is 4.
