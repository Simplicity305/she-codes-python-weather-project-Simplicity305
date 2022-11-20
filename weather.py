import csv
from datetime import datetime


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"



def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    date = datetime.fromisoformat(iso_string)
    formatted_date = date.strftime ("%A %d %B %Y")

    return formatted_date

    # ALTERNATIVE SOLUTION- concise, but not very readable
    # return datetime.fromisoformat(iso_string).strftime ("%A %d %B %Y")



def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    
    celsius = (float(temp_in_farenheit) - 32) * (5 / 9)

    return round(celsius, 1) 
    


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    total = 0

    for temp in weather_data:
        total += float(temp)
    mean = total / len(weather_data)

    return mean



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """    

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

    #What should happen if the length of line is less than 3? E.g. missing data? How should you account for that? Or does that depend on the type of data/what that data represents? Or would you input default values?

    # ALTERNATIVE SOLUTION - Using list comprehension, but harder to read
    # with open(csv_file, encoding="utf-8") as csv_file:
    #     next(csv_file)
    #     reader = csv.reader(csv_file)

    #     data = [[line[0], int(line[1]), int(line[2])] for line in reader if len(line) == 3]

    #     return data



def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    if len(weather_data) == 0:
        return ()

    min_index = 0
    min_temp = float(weather_data[0]) 

    enumerated_weather_data = enumerate(weather_data)

    for index, temp in enumerated_weather_data:
        temp = float(temp)

        if temp <= min_temp:
            min_temp = temp
            min_index = index

    return (min_temp, min_index) 



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """

    if len(weather_data) == 0:
        return ()

    max_index = 0
    max_temp = float(weather_data[0])

    enumerated_weather_data = enumerate(weather_data)

    for index, temp in enumerated_weather_data:
        temp = float(temp)
        
        if temp >= max_temp:
            max_temp = temp
            max_index = index

    return (max_temp, max_index)



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # number of days 
    num_of_days = len(weather_data)

    # min average
    min_list = [line[1] for line in weather_data]    
    mean_of_min_list = calculate_mean(min_list)
    formatted_min_mean = format_temperature(convert_f_to_c(mean_of_min_list))

    # min temp
    min_temp, min_index = find_min(min_list) 
    formatted_min = format_temperature(convert_f_to_c(min_temp))
    min_date = weather_data[min_index][0]
    formatted_min_date = convert_date(min_date)

    #max average
    max_list = [line[2] for line in weather_data]
    mean_of_max_list = calculate_mean(max_list)
    formatted_max_mean = format_temperature(convert_f_to_c(mean_of_max_list))

    # max temp
    max_temp, max_index = find_max(max_list)
    formatted_max = format_temperature(convert_f_to_c(max_temp))
    max_date = weather_data[max_index][0]
    formatted_max_date = convert_date(max_date)

    summary = (f"{num_of_days} Day Overview\n  The lowest temperature will be {formatted_min}, and will occur on {formatted_min_date}.\n  The highest temperature will be {formatted_max}, and will occur on {formatted_max_date}.\n  The average low this week is {formatted_min_mean}.\n  The average high this week is {formatted_max_mean}.\n")

    return summary

    # In normal circumstances, should we just be creating new functions for things like min/max average and min/max temp? 
    # Are there any suggestions for making my code in this section more concise?
    

    # ALTERNATIVE SOLUTION FOR MIN/MAX AVERAGE - Using standard for loop 
    # min_list = []
    # for line in weather_data:
    #     min_list.append(line[1])
    # mean_of_min_list = calculate_mean(min_list)
    # formatted_min_mean = format_temperature(convert_f_to_c(mean_of_min_list))



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    daily_summary = ""

    for daily_data in weather_data:
        date = convert_date(daily_data[0])
        min_temp = format_temperature(convert_f_to_c(daily_data[1]))
        max_temp = format_temperature(convert_f_to_c(daily_data[2]))
        
        daily_summary += f"---- {date} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n"

    return daily_summary