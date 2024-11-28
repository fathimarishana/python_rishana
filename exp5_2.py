from datetime import datetime
import time
current_datetime = datetime.now()
print("current date and time:",current_datetime)
print("current year:",current_datetime.year)
print("month of the year:",current_datetime.strftime("%B"))
print("week number of the year:",current_datetime.strftime("%U"))
print("weekday of the week:",current_datetime.strftime("%A"))
print("day of the year:",current_datetime.strftime("%j"))
print("day of the month:",current_datetime.day)
print("day of the week:",current_datetime.strftime("%A"))

