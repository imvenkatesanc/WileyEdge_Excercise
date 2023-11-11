def calculate_day_of_week(year, month, day):
    if month in (1, 2):
        month += 12
        year -= 1

    j = year // 100
    k = year % 100

    h = (day + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) - 2 * j) % 7

    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days_of_week[h]

def main():
    year = int(input("Enter year (e.g., 2012): "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter the day of the month (1-31): "))

    day_of_week = calculate_day_of_week(year, month, day)

    print(f"Day of the week is {day_of_week}")

if __name__ == "__main__":
    main()
