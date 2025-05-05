
from datetime import datetime

# Ensure the date format matches the string format
date_format = "It's %A, %B %d, %Y"

today_string = "It's Sunday, April 27, 2025"

parsed_date = datetime.strptime(today_string, date_format)

print(parsed_date)