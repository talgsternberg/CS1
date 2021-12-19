#Tal Sternberg
#CS1: lab2: checkpoint.py
#10/20/2019
#a file that reads data, creates objects, and writes them into a text file using __str__

from city import City
def make_cityobjectslist_and_create_and_output_file():
    #opening the file for reading
    in_file = open('world_cities.txt', 'r')

    cities = []

    for line in in_file:
        #strip each line of white characters and split at commas and divide into list
        parts = line.strip().split(',')
        cities.append(parts)

    #creating/storing objects for each city in out list
    city_objects = []

    for i in range(len(cities)):

        # create a city object using a constructor
        city = City(cities[i][0], cities[i][1], cities[i][2], cities[i][3], cities[i][4], cities[i][5])

        #add city object to list of city objects
        city_objects.append(city)

    #close in_file because we are done using it
    in_file.close()


    #preparing for writing an output file
    output_file = open('cities_out.txt', 'w')


    #add to output file info for each city object
    for i in range(len(city_objects)):
        output_file.write(str(city_objects[i]) + '\n')



    #close the output file
    output_file.close()

    return city_objects











