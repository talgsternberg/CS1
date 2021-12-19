#Tal Sternberg
#CS1
#10/22/2019
#quicksort.py
#building a partition and quicksort function to use on my list of city objects

from random import randint


#creating a partition function to implement for quicksort
def partition(the_list, p, r):
    n = randint(p,r)
    pivot = the_list[r]

    #randomizing pivot
    the_list[r], the_list[n] = the_list[n], the_list[r]

    i = p-1
    j = p
    while j < r:

        #if the list val is less than/equal to pivot
        if the_list[j] <= pivot:
            #increment i
            i += 1

            #swap the values
            the_list[i], the_list[j] = the_list[j], the_list[i]

        #increment j
        j += 1
    the_list[r], the_list[i+1] = the_list[i+1], the_list[r]

    return i+1


#create a quicksort function
def quicksort(the_list, p = 0, r = None):
    #assigning an r if none given
    if r is None:
        r = (len(the_list))-1

    #check base case -- if p exceeds r do nothing

    #recursive case
    if p < r:
        q = partition(the_list, p, r)  #returns i+1 to the value q
        quicksort(the_list, p, q-1) #quicksort the list less than pivot
        quicksort(the_list, q+1, r) #quicksort the list greater than pivot