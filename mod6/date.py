# date.py
# Logan Till 
# 2025-07-24

from datetime import date, datetime

today = date.today()
with open('today.txt', 'w') as file:
   file.write(today.isoformat())

with open('today.txt', 'r') as file:
   today_string = file.read()

fmt = "%Y-%m-%d"

parsed_date = datetime.strptime(today_string, fmt)
print(f"Parsed date is {parsed_date.date()}")
