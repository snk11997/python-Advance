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
specific_date = datetime.date(2024, 4, 9)
print("Specific date:", specific_date)

# Create a specific time
specific_time = datetime.time(14, 30, 0)
print("Specific time:", specific_time)

# Formatting dates and times
formatted_date = current_date.strftime("%Y-%m-%d")
print("Formatted date:", formatted_date)

formatted_time = current_time.strftime("%H:%M:%S")
print("Formatted time:", formatted_time)

# Parsing dates and times from strings
date_string = "2024-04-09"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
print("Parsed date:", parsed_date)

time_string = "14:30:00"
parsed_time = datetime.datetime.strptime(time_string, "%H:%M:%S").time()
print("Parsed time:", parsed_time)

# Date arithmetic
tomorrow = current_date + datetime.timedelta(days=1)
print("Tomorrow's date:", tomorrow)

one_week_later = current_date + datetime.timedelta(weeks=1)
print("One week later:", one_week_later)

# Time arithmetic
one_hour_later = (datetime.datetime.combine(datetime.date.today(), current_time) + datetime.timedelta(hours=1)).time()
print("One hour later:", one_hour_later)
