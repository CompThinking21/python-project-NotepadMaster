from __future__ import print_function
import time
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
            if element < pivot:
                subarray1.append(element)
            #to catch repeats
            #need to work out the kinks
            elif element == pivot:
                pivotarray.append(element)
            #if larger it goes into subarray 2
            else:
                subarray2.append(element)
        print('all elements less than pivot:', subarray1)
        print('The pivot/pivots', pivotarray)
        print('all elements greater than the pivot:', subarray2)
        time.sleep(3)
        #if len >0 so that uncessary empty lists are not recycled.
        if len(subarray1)>0:
            QuickSort(subarray1, Savearray)
        #THERE MUST ALWAY BE A PIVOT
        for x in pivotarray:
            xarray=[]
            xarray.append(x)
            QuickSort(xarray,Savearray)
        if len(subarray2)>0:
            QuickSort(subarray2,Savearray)
    #merging it all
    else:
        #print('The element appending:', array[0])
        time.sleep(1)
        Savearray.append(array[0])
    #return
    return Savearray
        
'''
Psudocode I got from "https://www.researchgate.net/figure/Pseudocode-of-quicksort-adapted-from-1_fig1_332434596"

'''

#main
print('Quicksort is a more complicated sorting algorthim')
time.sleep(2)
print('Although simple here we will introduce a concept of divide and conquer')
time.sleep(3)
print('What is divide and conquer? Well like RTS games this is to tackle the problem by breaking')
print('it into pieces and solving all the smaller compontents')
print('The hard part is combining the split problem into a unified solution')
time.sleep(3)
print("Let us look at Quicksort although quick it's time complexity is O(x^2)")
print('This is because although quick at the worst case scenario this algorthim becomes insertion sort')
time.sleep(3)
print("But enough of that how does it work you ask")
print("Well simple! First we pick a random pivot which is a random element from the array or list")
time.sleep(3)
print("Then EVERY element less than the pivot goes to the left")
print("Then EVERY element greather than the pivot goes to the right")
time.sleep(3)
print("Then we recursively call the function again to keep on doing this")
print("Eventually we should have all the elements from the least in the left to greatest in the right")
time.sleep(3)
print("Then we merge it all into a list as shown here. The list we will us is [6,90,7,8,53,5,3,98,9,5,123,90]")
print("During recursion the recursion called first ends first so the all array less than pivot will be recusively ongoing before the greater half")
time.sleep(3)
unsortlist=[6,90,7,8,53,5,3,98,9,5,123,90]
print(unsortlist)
sortedlist=[]
QuickSort(unsortlist, sortedlist)
print('This is the sorted array', sortedlist)
