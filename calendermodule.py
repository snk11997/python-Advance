import calendar

# Create a TextCalendar instance
cal = calendar.TextCalendar(calendar.SUNDAY)  # Specify the first day of the week (default is Monday)

# Print a month's calendar
year = 2024
month = 4
print(cal.formatmonth(year, month))

# # Print the calendar for the entire year
# print(cal.formatyear(year))

# # Check if a year is a leap year
# is_leap_year = calendar.isleap(year)
# print(f"{year} is a leap year: {is_leap_year}")

# # Get the day of the week for a specific date
# day_of_week = calendar.weekday(year, month, 24)  # year, month, day
# print(f"The day of the week for April 24, 2024 is: {calendar.day_name[day_of_week]}")

# # Get the number of days in a month
# num_days_in_month = calendar.monthrange(year, month)[1]
# print(f"Number of days in April 2024: {num_days_in_month}")  

# DATE AND TIME MODULE 

import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# Get the current date
current_date = datetime.date.today()
print("Current date:", current_date)

# Get the current time
current_time = datetime.datetime.now().time()
print("Current time:", current_time)

# Create a specific date
specific_date = datetime.date(2024, 4, 24)
print("Specific date:", specific_date)

# Create a specific time
specific_time = datetime.time(12, 30, 45)
print("Specific time:", specific_time)

# Combine date and time
combined_datetime = datetime.datetime.combine(specific_date, specific_time)
print("Combined datetime:", combined_datetime)

# Parse a string to datetime object
date_str = "2023-12-31"
parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed datetime:", parsed_date)

# Format a datetime object as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_datetime)

# Arithmetic operations with datetime
tomorrow = current_date + datetime.timedelta(days=1)
print("Tomorrow's date:", tomorrow)

# Time difference between two datetimes
time_diff = combined_datetime - current_datetime
print("Time difference:", time_diff)

