#Tal Sternberg
#CS1: lab2: read_data.py
#10/20/2019
#a file that reads data, creates objects, and writes them into a text file using __str__

from city import City
from quicksort import *
from checkpoint import *


city_objects = make_cityobjectslist_and_create_and_output_file()

def alphabetize(list):
    City.__le__ = City.compare_name
    in_abc = open('cities_alpha.txt', 'w')
    quicksort(list)
    for city in list:
        in_abc.write(str(city) + '\n')
    in_abc.close()


def organize_pop(list):
    City.__le__ = City.compare_population
    in_pop = open('cities_population.txt', 'w')
    quicksort(list)
    for city in list:
        in_pop.write(str(city) + '\n')
    in_pop.close()


def organize_lat(list):
    City.__le__ = City.compare_latitude
    in_lat = open('cities_latitude.txt', 'w')
    quicksort(list)
    for city in list:
        in_lat.write(str(city) + '\n')
    in_lat.close()


alphabetize(city_objects)
organize_lat(city_objects)
organize_pop(city_objects)





















