from __future__ import print_function
import time
import sys
import random
import re
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
        print('The pivot/pivots', pivotarray)
        print('all elements less than pivot:', subarray1)
        print('all elements greater than the pivot:', subarray2)
        print('')
        print('')
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
        print('')
        print('The element appending:', array[0])
        print('')
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
time.sleep(5)
print("Let us look at Quicksort although quick it's time complexity is O(x^2)")
print('This is because although quick at the worst case scenario this algorthim becomes insertion sort')
time.sleep(3)
print('This is done when each time the pivot picks the ends of the array essentially becoming insertion sort')
time.sleep(3)
print('In a randomized quicksort the chance of this is happening is 2/n')
print('Where n is the number of elements of the array')
time.sleep(3)
print('For those who forgot insertion sort it removes the end or the first element of the array')
time.sleep(3)
print('Moves it to the left if the pivot less than than the element left to it or right if it is greater than the element left to the pivot.')
time.sleep(4)
print('Hence it has a time of O(n^2)')
time.sleep(3)
print("But enough of this boring math stuff. How does it work you ask?")
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
print('')
sortedlist=[]
QuickSort(unsortlist, sortedlist)
print('')
print('This is the sorted array', sortedlist)
time.sleep(2)
print('')
print('So you maybe wondering what just happened?')
time.sleep(3)
print('Well let me explain')
print("This is a recursive implementation of randomized quicksort using python's random function")
time.sleep(3)
print('Hence when there is more than 1 element of it will recusrively call quicksort on the function')
print('Hence it goes in this order quicksort(elements_smaller) then quicksort(pivot_array) and then quicksort(elements_larger)')
time.sleep(5)
print('First it will go through quicksort(elements_smaller) to quickly sort all the elements less than the pivot')
print('When there is no other element (only one in the array) then it will be added into save list')
time.sleep(5)
print('From this implmentation a duplication (2 or more element of the same number) would cause')
print('An infinite loop because the exit condition is just "if the array has only 1 element" add it to the savearray')
time.sleep(5)
print('So essentially we divide first into a myriad of tiny pieces and combine them all after they are organized from least to greatest')
time.sleep(3)
#user turn
print('Now let us have you put in an array to visualize the algorthim')
print('Please enter numbers only into this query.')
print('After you are done putting the number please put spaces or punctuation between them')
print('To signify you are done with your query')
print('After you are done with the numbers for our array please press "enter"')
userstring=input('Please enter numbers here:')
userlist=[]
regextedstringsofnumbers=re.findall(r"\b[0-9]+\b", userstring)
for x in regextedstringsofnumbers:
    y=int(x)
    userlist.append(y)
sortedlist=[]
#calling quiksort on user's list
QuickSort(userlist, sortedlist)
print(sortedlist)
time.sleep(15)
