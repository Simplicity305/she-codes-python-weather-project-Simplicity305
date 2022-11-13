import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


# def format_temperature(temp):
#     """Takes a temperature and returns it in string format with the degrees
#         and celcius symbols.

#     Args:
#         temp: A string representing a temperature.
#     Returns:
#         A string contain the temperature and "degrees celcius."
#     """
#     return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass


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


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass


# def load_data_from_csv(csv_file):
#     data = []

#     with open(csv_file, encoding="utf-8") as csv_file:
#         next(csv_file)
#         reader = csv.reader(csv_file)
#         for line in reader:
#             if len(line) == 3:
#                 date = line[0]
#                 min = int(line[1])
#                 max = int(line[2])
#                 data.append([date, min, max]) 
#     return data

#     # How would you handle this if the data is not always 3 columns? eg future proofing - also try to reformat so the variable is (date, min, max) and try to play around with where you'd specify the int
# 

#     """Reads a csv file and stores the data in a list.

#     Args:
#         csv_file: a string representing the file path to a csv file.
#     Returns:
#         A list of lists, where each sublist is a (non-empty) line in the csv file.
#     """
#     pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
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