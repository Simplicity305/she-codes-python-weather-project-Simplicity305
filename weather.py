import csv
from datetime import datetime


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# -------------DONE----------------
def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

# -------------DONE----------------
def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    formatted_date = date.strftime ("%A %d %B %Y")
    return formatted_date


    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass

# ---------------DONE---------------
def convert_f_to_c(temp_in_farenheit):
    celsius = (float(temp_in_farenheit) - 32) * (5 / 9)
    return round(celsius, 1) 
    
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    pass

# -----------DONE---------------
def calculate_mean(weather_data):
    total = 0
    for temp in weather_data:
        total += float(temp)
    mean = total / len(weather_data)
    return mean


    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass


# ----------------DONE-----------------
def load_data_from_csv(csv_file):
    data = []

    with open(csv_file, encoding="utf-8") as csv_file:
        next(csv_file)
        reader = csv.reader(csv_file)
        for line in reader:
            if len(line) == 3:
                date = line[0]
                min = int(line[1])
                max = int(line[2])
                data.append([date, min, max]) 
    return data

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass



# ----------------DONE-----------------
def find_min(weather_data):
    if len(weather_data) == 0:
        return ()

    min_index = 0
    minimum = float(weather_data[0])

    enumerated_weather_data = enumerate(weather_data)

    for data in enumerated_weather_data:
        index, temp = data
        temp = float(temp)

        if temp <= minimum:
            minimum = temp
            min_index = index

    return (minimum, min_index)


    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass



# ----------------DONE-----------------
def find_max(weather_data):
    if len(weather_data) == 0:
        return ()

    max_index = 0
    maximum = float(weather_data[0])

    enumerated_weather_data = enumerate(weather_data)

    for data in enumerated_weather_data:
        index, temp = data
        temp = float(temp)
        
        if temp >= maximum:
            maximum = temp
            max_index = index

    return (maximum, max_index)

    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
