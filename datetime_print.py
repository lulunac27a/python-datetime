import datetime as dt

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))
hour = int(input("Hour: "))
minute = int(input("Minute: "))
second = int(input("Second: "))
microsecond = int(input("Microsecond: "))

entered_datetime = dt.datetime(
    year, month, day, hour, minute, second, microsecond
)  # Retrieve date and time input values
print(
    f"Weekday: {entered_datetime:%a} ({entered_datetime:%A}) Number: {entered_datetime:%w}"
)
print(f"Day of month: {entered_datetime:%d}")
print(
    f"Month: {entered_datetime:%b} ({entered_datetime:%B}) Number: {entered_datetime:%m}"
)
print(f"Year: {entered_datetime:%Y} ('{entered_datetime:%y})")
print(
    f"Hour: {entered_datetime:%H} ({entered_datetime:%I} {entered_datetime:%p})")
print(f"Minute: {entered_datetime:%M}")
print(f"Second: {entered_datetime:%S}")
print(f"Microsecond: {entered_datetime:%f}")
print(f"UTC offset: {entered_datetime:%z}")
print(f"Time zone: {entered_datetime:%Z}")
print(f"Day of year: {entered_datetime:%j}")
print(f"Week number (week starts on Sunday): {entered_datetime:%U}")
print(f"Week number (week starts on Monday): {entered_datetime:%W}")
print(f"Locale date and time: {entered_datetime:%c}")
print(f"Locale date: {entered_datetime:%x}")
print(f"Locale time: {entered_datetime:%X}")
print("Time offset:", dt.datetime.astimezone(entered_datetime).tzinfo)
print("Full date and time with time zone:",
      dt.datetime.astimezone(entered_datetime))

now: dt.datetime = dt.datetime.now()  # Get current date and time
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

utc: dt.datetime = dt.datetime.now(
    dt.timezone.utc)  # Get current UTC date and time
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
