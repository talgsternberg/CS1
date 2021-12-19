#Tal Sternberg
#10/20/2019
#CS1: Lab2: city.py
#defining a city class

class City:
    #define/initialize instance vars
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.code = country_code
        self.name = name
        self.region = region
        self.pop = int(population)
        self.lat = float(latitude)
        self.long = float(longitude)


    #string method to return when print is called on an object
    def __str__(self):
        return self.name + ", " + str(self.pop) + ", " + str(self.lat) + ", " + str(self.long)


    #comparing populations
    def compare_population(self, other):
        if other.pop <= self.pop:
            return True

   #comparing names
    def compare_name(self, other):
        if self.name.lower() <= other.name.lower():
            return True

    #comparing latitudes
    def compare_latitude(self, other):
        if self.lat <= other.lat:
            return True




