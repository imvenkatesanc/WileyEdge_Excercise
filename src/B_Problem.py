recievedMinutes = int(input("Enter minutes: "))

# mins calculation

minutes_per_day = 24*60
minutes_per_week = minutes_per_day*7
minutes_per_month = minutes_per_day*30
minutes_per_year = minutes_per_day*365

#calculation based on user input

year = (recievedMinutes)//minutes_per_year
month = (recievedMinutes%minutes_per_year)//minutes_per_month
week = (recievedMinutes%minutes_per_month)//minutes_per_week
day = (recievedMinutes%minutes_per_month)//minutes_per_day

print(f"{recievedMinutes} minutes is approximately {year} years, {month} months, {week} weeks and {day} days.")