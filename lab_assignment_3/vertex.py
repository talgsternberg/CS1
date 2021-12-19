#Tal Sternberg
#CS 1
#vertex.py for lab3: creates a vertex class
#11/3/2019

from cs1lib import *

#global vars for drawing my verticies and edges that I will use in later methods
RADIUS = 5
STROKE_WIDTH = 3

class Vertex:

    #initializing instance vars
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adjacency = []



    # method to create list of adj vals
    def append(self, adj):
        self.adjacency.append(adj)


    #getter methods
    def get_name(self):
        return self.name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_neighbors(self):
        return self.adjacency



    #a string method for when I print object
    def __str__(self):
        #break up the adj list into strings
        string_adj = ''
        for i in range(len(self.adjacency)):
            if i == len(self.adjacency) - 1:
                string_adj += self.adjacency[i].name
            else:
                string_adj += self.adjacency[i].name + ', '
        #return what i want printed
        return self.name + '; ' + 'Location: ' + str(self.x) + ', ' + str(self.y) + '; ' + 'Adjacent vertices: ' + string_adj

    #draw circle for each vertex
    def draw_vert(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, RADIUS)

    #draw single line (to be called in my draw neighbors method
    def draw_edge(self, r, g, b, vertex):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(STROKE_WIDTH)
        draw_line(self.x, self.y, vertex.get_x(), vertex.get_y())

    #draw all lines
    def draw_edge_neighbors(self, r, g, b):
        for neighbor in self.adjacency:
            #call my other method declared above
            self.draw_edge(r, g, b, neighbor)


    # draw the name of the location (for extra credit purposes)
    def draw_name(self):
        enable_stroke()
        set_font_size(20)
        draw_text(self.name, self.x, self.y)



    #method to find mouse intersect vertex
    def in_radius(self, mouse_x, mouse_y):
        return (self.x-RADIUS <= mouse_x <= self.x+RADIUS) and (self.y-RADIUS <= mouse_y <= self.y+RADIUS)






