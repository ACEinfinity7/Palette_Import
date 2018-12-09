"""
functions to read the a CSV file
and put it into a dictionary
"""
import os
import csv

def read_palette_from_file(palette_filename):
    """
    read the palette from the csv file.
    Each row is a key and an RGB triple.  Make that RGB triple
    into a TUPLE and then put into a dictionary with the key.
    """
    my_dict = dict()
    with open (palette_filename, 'r') as pallatte:
        pallatte_csv_reader = csv.reader(pallatte)
        for row in pallatte_csv_reader:
            key = int(row[0])
            red_value = int(row[1])
            green_value = int(row[2])
            blue_value = int(row[3])

            pallatte_tuple = (red_value, green_value, blue_value)

            my_dict[key] = pallatte_tuple


    return my_dict
