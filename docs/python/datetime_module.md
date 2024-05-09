#### [Return Back](../../python_for_testers.md)

# Datetime Module

The `datetime` module in Python provides classes and functions for working with dates and times. It allows you to create, manipulate, and format dates, times, and timedeltas. The `datetime` module is part of the Python standard library, so there's no need to install any external packages to use it.

### Basic Usage:

To use the `datetime` module, you need to import it:

```python
import datetime
```

### Datetime Class:

The `datetime` class represents a specific date and time. It has the following attributes: year, month, day, hour, minute, second, microsecond, and timezone (optional).

```python
# Create a datetime object for the current date and time
current_datetime = datetime.datetime.now()

# Create a datetime object for a specific date and time
specific_datetime = datetime.datetime(2023, 12, 31, 23, 59, 59)

# Access datetime attributes
year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute
second = current_datetime.second
microsecond = current_datetime.microsecond

# Print the datetime object
print(current_datetime)
```

### Date Class:

The `date` class represents a specific date (year, month, and day) without time information.

```python
# Create a date object for the current date
current_date = datetime.date.today()

# Create a date object for a specific date
specific_date = datetime.date(2023, 12, 31)

# Access date attributes
year = current_date.year
month = current_date.month
day = current_date.day

# Print the date object
print(current_date)
```

### Time Class:

The `time` class represents a specific time (hour, minute, second, and microsecond) without date information.

```python
# Create a time object for the current time
current_time = datetime.datetime.now().time()

# Create a time object for a specific time
specific_time = datetime.time(23, 59, 59)

# Access time attributes
hour = current_time.hour
minute = current_time.minute
second = current_time.second
microsecond = current_time.microsecond

# Print the time object
print(current_time)
```

### Timedelta Class:

The `timedelta` class represents the difference between two dates or times. It's useful for performing arithmetic operations on dates and times.

```python
# Create a timedelta object representing 1 day
one_day = datetime.timedelta(days=1)

# Add a timedelta to a date or datetime
tomorrow = datetime.date.today() + one_day

# Subtract two datetimes to get a timedelta
delta = datetime.datetime(2023, 12, 31) - datetime.datetime.now()

# Print the timedelta object
print(delta)
```

### Formatting Dates and Times:

You can format dates and times using the `strftime()` method (string format time).

```python
formatted_date = current_date.strftime("%Y-%m-%d")
formatted_time = current_time.strftime("%H:%M:%S")
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_date)
print(formatted_time)
print(formatted_datetime)
```

### Parsing Dates and Times:

You can parse strings into datetime objects using the `strptime()` method (string parse time).

```python
date_string = "2023-12-31"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")

print(parsed_date)
```

### Timezone Handling:

The `datetime` module also provides functionality for working with timezones through the `timezone` class and `astimezone()` method.

```python
# Create a timezone object for UTC
utc_timezone = datetime.timezone.utc

# Convert a datetime to a different timezone
datetime_with_timezone = current_datetime.astimezone(utc_timezone)
```

These are the basic functionalities provided by the `datetime` module. It's a powerful and versatile module for handling dates, times, and timedeltas in Python. You can explore more advanced features and options in the Python documentation.
