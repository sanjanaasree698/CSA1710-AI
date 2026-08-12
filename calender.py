# Python Program to Generate Calendar for a Given Month and Year

import calendar

# Input month and year
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Display calendar
print("\nCalendar:")
print(calendar.month(year, month))