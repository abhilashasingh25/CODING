# python program to write date and time using dateutil module

from dateutil import parser

date_time = parser.parse("Mar 11 2025 11:31 AM")
print(date_time)
print(type(date_time))