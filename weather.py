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

# (0, 49) - 1st loop - 
# (1, 57) - 2nd - 
# (2, 56) - 
# (3, 55)
# (4, 10) - 

    min_index = 4
    minimum_temp = 10

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


# ----------------DONE---------------
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
    # number of days 
    num_days = len(weather_data)

    # min average
    min_list = []
    for line in weather_data:
        min_list.append(line[1])
    mean_min = calculate_mean(min_list)
    formatted_mean_min = format_temperature(convert_f_to_c(mean_min))
    
    # min temp
    min_temp, min_index = find_min(min_list) 
    formatted_min = format_temperature(convert_f_to_c(min_temp))
    min_date = weather_data[min_index][0]
    formatted_min_date = convert_date(min_date)

    #max average
    max_list = [line[2] for line in weather_data]
    mean_max = calculate_mean(max_list)
    formatted_mean_max = format_temperature(convert_f_to_c(mean_max))

    # max_temp
    max_temp, max_index = find_max(max_list)
    formatted_max = format_temperature(convert_f_to_c(max_temp))
    max_date = weather_data[max_index][0]
    formatted_max_date = convert_date(max_date)

    # # min average
    # min_list = []
    # for line in weather_data:
    #     min_list.append(line[1])
    # mean_min = calculate_mean(min_list)
    # formatted_mean_min = format_temperature(mean_min)

    return (f"{num_days} Day Overview\n  The lowest temperature will be {formatted_min}, and will occur on {formatted_min_date}.\n  The highest temperature will be {formatted_max}, and will occur on {formatted_max_date}.\n  The average low this week is {formatted_mean_min}.\n  The average high this week is {formatted_mean_max}.\n")


    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):

    daily_summary = ""

    for daily_data in weather_data:
        date = convert_date(daily_data[0])
        min_temp = format_temperature(convert_f_to_c(daily_data[1]))
        max_temp = format_temperature(convert_f_to_c(daily_data[2]))
        
        daily_summary += f"---- {date} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n"

    # print(daily_summary)

    return daily_summary
    

# ---- Friday 02 July 2021 ----
#   Minimum Temperature: 9.4°C
#   Maximum Temperature: 19.4°C

# ---- Saturday 03 July 2021 ----
#   Minimum Temperature: 13.9°C
#   Maximum Temperature: 20.0°C

# ---- Sunday 04 July 2021 ----
#   Minimum Temperature: 13.3°C
#   Maximum Temperature: 16.7°C

# ---- Monday 05 July 2021 ----
#   Minimum Temperature: 12.8°C
#   Maximum Temperature: 16.1°C

# ---- Tuesday 06 July 2021 ----
#   Minimum Temperature: 11.7°C
#   Maximum Temperature: 16.7°C
    

    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

