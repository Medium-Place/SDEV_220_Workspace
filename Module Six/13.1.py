from datetime import date

today = date.today()

today_string = today.isoformat()

with open('today.txt', 'w') as file: 
    file.write(today_string)
