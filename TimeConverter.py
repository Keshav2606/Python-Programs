def convert_time(time_str):
    time_str = time_str.strip()  # Clears the white spaces
    hour, min = time_str[:-2].split(':')
    hour = int(hour)
    min = int(min)
    period = time_str[-2:]

    if period.lower() == 'pm' and hour != 12:
        hour += 12
    elif period.lower() == 'am' and hour == 12:
        hour = 0
    return f"{hour:02d}:{min:02d}"


print(convert_time("10:30 pm"))
print(convert_time("09:45 am"))
print(convert_time("12:30 pm"))
print(convert_time("12:45 am"))
