#Tal Sternberg
#CS 1
#load_graph.py for lab3: creates a graphical map
#11/3/2019

from vertex import *

def load_graph(file):
    vertex_objects_dict = {}
    file_name = open(file, "r")

    #separating all three items
    for line in file_name:
        #split semicolons
        new_line = line.split('; ')

        #make 2nd index a list (x and y)
        new_line_list = new_line[2].split(', ')

        #make the objects
        new_vert = Vertex(new_line[0], new_line_list[0], new_line_list[1])


        #add to dict
        vertex_objects_dict[new_line[0]] = new_vert
    file_name.close()

    file_name = open(file, "r")
    #2nd pass
    for line in file_name:
        # split semicolons
        new_line = line.split('; ')

        x = new_line[1].split(", ")

        #turn adjacent list from a list of strings into a list of vertices
        for i in range(len(x)):
            vertex_objects_dict[new_line[0]].append(vertex_objects_dict[x[i].strip()])
    file_name.close()

    return vertex_objects_dict



