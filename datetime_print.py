import datetime as dt
from datetime import datetime

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))
hour = int(input("Hour: "))
minute = int(input("Minute: "))
second = int(input("Second: "))
microsecond = int(input("Microsecond: "))

entered = dt.datetime(
    year, month, day, hour, minute, second, microsecond
)  # Retrieve date and time input values
print(f"Weekday: {entered:%a} ({entered:%A}) Number: {entered:%w}")
print(f"Day of month: {entered:%d}")
print(f"Month: {entered:%b} ({entered:%B}) Number: {entered:%m}")
print(f"Year: {entered:%Y} ('{entered:%y})")
print(f"Hour: {entered:%H} ({entered:%I} {entered:%p})")
print(f"Minute: {entered:%M}")
print(f"Second: {entered:%S}")
print(f"Microsecond: {entered:%f}")
print(f"UTC offset: {entered:%z}")
print(f"Time zone: {entered:%Z}")
print(f"Day of year: {entered:%j}")
print(f"Week number (week starts on Sunday): {entered:%U}")
print(f"Week number (week starts on Monday): {entered:%W}")
print(f"Locale date and time: {entered:%c}")
print(f"Locale date: {entered:%x}")
print(f"Locale time: {entered:%X}")
print("Time offset:", dt.datetime.astimezone(entered).tzinfo)
print("Full date and time with time zone:", dt.datetime.astimezone(entered))

now: datetime = dt.datetime.now()  # Get current date and time
print(f"Current Weekday: {now:%a} ({now:%A}) Number: {now:%w}")
print(f"Current Day of month: {now:%d}")
print(f"Current Month: {now:%b} ({now:%B}) Number: {now:%m}")
print(f"Current Year: {now:%Y} ('{now:%y})")
print(f"Current Hour: {now:%H} ({now:%I} {now:%p})")
print(f"Current Minute: {now:%M}")
print(f"Current Second: {now:%S}")
print(f"Current Microsecond: {now:%f}")
print(f"Current UTC offset: {now:%z}")
print(f"Current Time zone: {now:%Z}")
print(f"Current Day of year: {now:%j}")
print(f"Current Week number (week starts on Sunday): {now:%U}")
print(f"Current Week number (week starts on Monday): {now:%W}")
print(f"Current Locale date and time: {now:%c}")
print(f"Current Locale date: {now:%x}")
print(f"Current Locale time: {now:%X}")
print("Time offset:", dt.datetime.astimezone(now).tzinfo)
print("Full date and time with time zone:", dt.datetime.astimezone(now))

# Get current UTC date and time
utc: datetime = dt.datetime.now(dt.timezone.utc)
print(f"Current UTC Weekday: {utc:%a} ({utc:%A}) Number: {utc:%w}")
print(f"Current UTC Day of month: {utc:%d}")
print(f"Current UTC Month: {utc:%b} ({utc:%B}) Number: {utc:%m}")
print(f"Current UTC Year: {utc:%Y} ('{utc:%y})")
print(f"Current UTC Hour: {utc:%H} ({utc:%I} {utc:%p})")
print(f"Current UTC Minute: {utc:%M}")
print(f"Current UTC Second: {utc:%S}")
print(f"Current UTC Microsecond: {utc:%f}")
print(f"Current UTC UTC offset: {utc:%z}")
print(f"Current UTC Time zone: {utc:%Z}")
print(f"Current UTC Day of year: {utc:%j}")
print(f"Current UTC Week number (week starts on Sunday): {utc:%U}")
print(f"Current UTC Week number (week starts on Monday): {utc:%W}")
print(f"Current UTC Locale date and time: {utc:%c}")
print(f"Current UTC Locale date: {utc:%x}")
print(f"Current UTC Locale time: {utc:%X}")
print("Time offset:", dt.datetime.astimezone(utc).tzinfo)
print("Full date and time with time zone:", dt.datetime.astimezone(utc))
