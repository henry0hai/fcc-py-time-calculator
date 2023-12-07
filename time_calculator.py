def add_time(start, duration, day=None):
    """
    Adds a duration to a starting time and returns the ending time.

    Args:
        start (str): The starting time in the format "HH:MM AM/PM".
        duration (str): The duration in the format "HH:MM".
        day (str, optional): The day of the week (case-insensitive).

    Returns:
        str: The ending time in the format "HH:MM AM/PM", optionally followed by the day of the week and the number of days later.

    Raises:
        ValueError: If the start time is invalid.

    Example Usage:
        add_time("11:30 AM", "2:15")  # Returns "1:45 PM"
        add_time("9:15 PM", "5:30")  # Returns "2:45 AM (next day)"
        add_time("11:55 AM", "3:12")  # Returns "3:07 PM"
        add_time("12:00 PM", "0:01")  # Returns "12:01 PM"
        add_time("6:30 PM", "205:12")  # Returns "7:42 AM (9 days later)"
        add_time("3:00 PM", "3:10")  # Returns "6:10 PM"
        add_time("2:59 AM", "24:00")  # Returns "2:59 AM (next day)"
        add_time("11:59 PM", "24:05")  # Returns "12:04 AM (2 days later)"
        add_time("8:16 PM", "466:02")  # Returns "6:18 AM (20 days later)"
    """

    days_of_week = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    am_pm = {"AM": 0, "PM": 12}
    try:
        start_time, period = start.split()
        start_hour, start_minute = map(int, start_time.split(":"))
        start_hour += am_pm[period]
    except ValueError as err:
        raise ValueError("Invalid Start Time") from err

    duration_hour, duration_minute = map(int, duration.split(":"))
    end_minute = (start_minute + duration_minute) % 60
    carry_hour = (start_minute + duration_minute) // 60
    end_hour = (start_hour + duration_hour + carry_hour) % 24
    days_later = (start_hour + duration_hour + carry_hour) // 24

    if end_hour < 12:
        end_period = "AM"
    else:
        end_hour -= 12
        end_period = "PM"
    if end_hour == 0:
        end_hour = 12

    end_time = f"{end_hour}:{end_minute:02d} {end_period}"
    if day:
        day_index = (days_of_week.index(day.lower()) + days_later) % 7
        end_time += f", {days_of_week[day_index].capitalize()}"

    if days_later == 1:
        end_time += " (next day)"
    elif days_later > 1:
        end_time += f" ({days_later} days later)"

    return end_time
