import sys
import random
#had to push the system beyond.
sys.setrecursionlimit(10000)
#quicksort can only accept lists or arrays
#the recursive crackhead method
def QuickSort(array, Savearray):
    #if condition so that as long as array size is greater than 1
    #do the rest of the function
    if len(array)>1:
        #picking a random pivot of the array
        pivot = random.choice(array)
        #creation of recursive lists
        subarray1 = []
        subarray2 = []
        pivotarray = []
        #for loop to get every single element of array
        for element in array:
            #if smaller or equal to pivot put in subarray1
            if element <= pivot:
                subarray1.append(element)
            #to catch repeats
            #need to work out the kinks
##            elif element == pivot:
##                pivotarray.append(pivot)
            #if larger it goes into subarray 2
            else:
                subarray2.append(element)
##        print(subarray1)
##        print(subarray2)
        #if len >0 so that uncessary empty lists are not recycled.
        if len(subarray1)>0:
            QuickSort(subarray1, Savearray)
        if len(subarray2)>0:
            QuickSort(subarray2,Savearray)
    #merging it all
    else:        
        Savearray.append(array[0])
    #return
    return Savearray
        
'''
Psudocode I got from "https://www.researchgate.net/figure/Pseudocode-of-quicksort-adapted-from-1_fig1_332434596"

'''

#main
unsortlist=[6,90,7,8,53,5,3,98,9,123]
sortedlist=[]
QuickSort(unsortlist, sortedlist)
print(sortedlist)
