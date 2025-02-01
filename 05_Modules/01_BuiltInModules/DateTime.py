# Module to work with date and time in python                                        |
#------------------------------------------------------------------------------------|
import datetime                                             # Import module          |
now = datetime.datetime.now()                               # Current date & time    |
print(f"Current: {now}")                                    # Print full datetime    |
today = datetime.date.today()                               # Today's date           |
print(f"Date: {today}")                                     # Print date only        |
current_time = now.time()                                   # Extract time only      |
print(f"Time: {current_time}")                              # Print time             |
year = today.year                                           # Get current year       |
month = today.month                                         # Get current month      |
day = today.day                                             # Get current day        |
print(f"Year: {year}, Month: {month}, Day: {day}")          # Print year, month, day |
weekday = today.strftime("%A")                              # Get current weekday    |
print(f"Today is: {weekday}")                               # Print weekday          |
formatted = now.strftime("%d/%m/%Y %H:%M:%S")               # Format date & time     |   
print(f"Formatted: {formatted}")                            # Print formatted date   |
one_week_later = today + datetime.timedelta(weeks=1)        # Add 1 week             |
print(f"In one week: {one_week_later}")                     # Print new date         |
yesterday = today - datetime.timedelta(days=1)              # Subtract 1 day         |
print(f"Yesterday was: {yesterday}")                        # Print past date        |
date1, date2 = datetime.date(2024, 1, 1),datetime.date(2024, 12, 31)                #| 
diff = (date2 - date1).days                                 # Days between dates     |
print(f"Days between {date1} and {date2}: {diff}")          # Print day difference   |
is_leap = today.year % 4 == 0 and (today.year % 100 != 0 or today.year % 400 == 0)  #|
print(f"Is {today.year} a leap year? {is_leap}")            # Check if year is leap y|
# -- Terminal Output ----------------------------------------------------------------|
#Current: 2025-02-01 14:58:23.637326                                                 |                    
#Date: 2025-02-01                                                                    |
#Time: 14:58:23.637326                                                               |                                                        
#Year: 2025, Month: 2, Day: 1                                                        |
#Today is: Saturday                                                                  |
#Formatted: 01/02/2025 14:58:23                                                      |
#In one week: 2025-02-08                                                             |                             
#Yesterday was: 2025-01-31                                                           |
#Days between 2024-01-01 and 2024-12-31: 365                                         |
#Is 2025 a leap year? False                                                          |
#====================================================================================|
