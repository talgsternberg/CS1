#Tal Sternberg
#CS 1
#map_plot.py for lab3: creates a graphical map
#11/3/2019

from cs1lib import *
from checkpoint import vertex_dict
from vertex import *
from bfs import *

#setting window to fit image
WIDTH = 1012
HEIGHT = 811


#x and y of mouse
x = 0
y = 0


#start and end verticies
start_vertex = None
end_vertex = None

img = load_image('dartmouth_map.png')

#when mouse is down
def mouse_down(mx, my):
    global x, y, start_vertex
    x = mx
    y = my
    start_vertex = None

    #determine if we should reassign start vertex
    for key in vertex_dict:
        if vertex_dict[key].in_radius(x, y):  # should i draw red circle on press??
            start_vertex = vertex_dict[key]



#when mouse is moving
def mouse_move(mx, my):
    global x, y, start_vertex, end_vertex
    x = mx
    y = my
    end_vertex = None

    #if start vertex isnt none and mouse is on a vertex, find end vertex
    if start_vertex != None:
        for key in vertex_dict:
            if vertex_dict[key].in_radius(x, y):
                end_vertex = vertex_dict[key]



#function that draws everything
def draw_map():
    global start_vertex, end_vertex

    draw_image(img, 0, 0)
    for key in vertex_dict:
        vertex_dict[key].draw_vert(0,0,1) #draw the circle
        vertex_dict[key].draw_edge_neighbors(0,0,1) #draw the lines

    #draw start vertext if not none
    if start_vertex != None:
        start_vertex.draw_vert(1,0,0)

    #draw end vertex if not none and start vertex exists
    if end_vertex != None and start_vertex != None:
        end_vertex.draw_vert(1, 0, 0)

        #draw lines red for bfs (ONLY IF START AND END VERTEX ARE NOT NONE!!)
        path = bfs(start_vertex, end_vertex)
        for i in range(len(path) - 1):
            path[i].draw_vert(1, 0, 0)
            path[i].draw_edge(1, 0, 0, path[i + 1])




start_graphics(draw_map, width=WIDTH, height=HEIGHT, mouse_press=mouse_down, mouse_move=mouse_move)