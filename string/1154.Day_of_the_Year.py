# Example 1:

# Input: 
date1 = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
# Example 2:

# Input: 
date2 = "2019-02-10"
# Output: 41

from datetime import datetime

def dayOfYear(date: str) -> int:
    year, month, day = map(int, date.split('-'))
    return int((datetime(year, month, day) - datetime(year, 1, 1)).days) + 1

print(dayOfYear(date1))
print(dayOfYear(date2))

def dayOfYear(date: str) -> int:
    year=int(date[:4])
    month=int(date[5:7])
    day=int(date[8:10])
    daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        daysOfMonth[1] = 29
    return sum(daysOfMonth[:month - 1]) + day

print(dayOfYear(date1))
print(dayOfYear(date2))