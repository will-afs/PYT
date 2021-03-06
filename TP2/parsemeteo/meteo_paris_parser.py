import os
import sys
import statistics
import argparse

def extract_column_values(raw_data, col_num):
    lines = raw_data.split('\n')
    column_values = []
    for line in lines[3:-1] : # values start from line n°3
        values = line.split()
        try:
            float(values[col_num])
        except ValueError:
            pass # print ("Not a float : " + values[col_num])
        else:
            column_values.append(float(values[col_num]))
    # print(column_values)
    return column_values
    

if __name__ == "__main__":
    print()

    parser = argparse.ArgumentParser(description='Processes statistical functions onto a file respecting Paris Meteo format')

    parser.add_argument('file_path', type=str,
                    help='The path of the file containing raw meteo data') # , metavar='F', , nargs='1'

    parser.add_argument('-c', '--column_number', type=int, nargs='?',
                help='The number of the column to process')              

    # parser.add_argument('--sum', metavar='S', type=str, nargs='*',
    #                 help='The type of action to execute on the column.')

    args = parser.parse_args()

    meteo_paris_file_path = args.file_path
    column_number = args.column_number
    
    try:
        with open(meteo_paris_file_path, 'r') as meteo_raw_data_file:
            meteo_raw_data = meteo_raw_data_file.read()
        # print(meteo_raw_data)

        high_temp_column = extract_column_values(meteo_raw_data, 3)
        try:
            max_temp_value = max(high_temp_column)
        except ValueError:
            max_temp_value = '?'
            print("There is no temperature value in column n°", 3, ".")
        print("The maximal temperature is : ", max_temp_value, "°C.\n")

        low_temp_column = extract_column_values(meteo_raw_data, 4)
        try:
            min_temp_value = min(low_temp_column)
        except ValueError:
            min_temp_value = '?'
            print("There is no temperature value in column n°", 4, ".")
        print("The minimal temperature is : ", min_temp_value, "°C.\n")

        current_temp_column = extract_column_values(meteo_raw_data, 2)
        try:
            standard_deviation = statistics.stdev(current_temp_column)
        except ValueError:
            standard_deviation = '?'
            print("There is no temperature value in column n°", 2, ".")
        print("The standard deviation of 'Temperature Out' column is : ", standard_deviation, ".\n")

    except FileNotFoundError:
        print('File does not exist.')       