from cs1lib import *


#loading background image
img = load_image('world.png')
CITIES_TO_VISUALIZE = 50

#creating a list of cities lists
def make_cities_list(n):
    in_pop = open('cities_population.txt', 'r')
    items_for_city = []
    lines_read = 0
    for line in in_pop:
        if lines_read > n:
            break
        items = line.strip().split(', ')
        items_for_city.append(items)
        lines_read += 1
    in_pop.close()
    return items_for_city


#assigning a variable to local list created in function above
cities_list = make_cities_list(CITIES_TO_VISUALIZE)

#what city index in list are we on? ie: which city should we be drawing and what "old" cities should we be drawing?
city_on = 0
old_cities = []

def main():
    global city_on, old_cities

    #make sure city is only in the first 50
    if city_on < CITIES_TO_VISUALIZE:
        draw_image(img, 0, 0)


        #draw old city on each old city location (blue dot)
        draw_old()

        #draw new city  on "new" city location
        set_fill_color(0,0,1)
        x = 2*float(cities_list[city_on][3]) + 360
        y = float(cities_list[city_on][2])*(-2) + 180
        draw_circle(x, y, 5)




        #old cities appending
        old_cities.append((x,y))

        #move on to the next city
        city_on += 1

#a function to draw all of the old cities that we will call in main
def draw_old():
    set_fill_color(0,0,1)
    for city in old_cities:
        #use the x/y values stored in my old_cities list saved from main
        draw_circle(city[0], city[1], 5)



start_graphics(main, framerate = 1.3, width = 720, height = 360)
