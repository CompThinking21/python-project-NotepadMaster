from __future__ import print_function
#for sleep()
import time
#for reasons
import sys
#for regexin'
import re

#must be arrays (lists) only
#could be optimized with minheapify
def SelectionSort(array):
    #while loop
    sortarray=[]
    #while the original array is not empty
    while len(array) !=0:
        #getting the pseudosmallest from the first element
        smallest=array[0]
        #for loop to find the smallest element
        for num in range(1,len(array)):
            if array[num]<smallest:
                smallest=array[num]
        #appening the the smallest into the sorted array
        sortarray.append(smallest)
        #removing the smallest from the array
        array.remove(smallest)
        #printing results
        print("")
        print("the smallest number is", smallest)
        print (sortarray, end='')
        print (array)
        print("")
        time.sleep(2)
    return sortarray

#main
print("Welcome to Selection Sort module also called bubble sort.")
time.sleep(3)
print('What is selection sort? Simple it is the simplest sorting algoeithm known to man.')
time.sleep(3)
print('The idea is very simple it is essentially like sorting a hand of cards.')
time.sleep(3)
print('It is getting a hand of cards and moving the smallest value to your other hand.')
time.sleep(3)
print('You keep on doing this until your original hand has no more cards.')
time.sleep(3)
print('As an example let me make a list [7,4,5,7,2,6,8,3].')
print('So essentially:')
time.sleep(4)
print("Sorted:[]")
print('unsorted:[7,4,5,7,2,6,8,3]')
print('We find the smallest number of the unsorted which is [2].')
print('This can be done through a for loop {costing n time} or minheapify {Costing lg(n) time}.')
time.sleep(10)
print('Thence we can move that over to the sorted list.')
print('Since it goes in order it does of smallest the list will be sorted from least to greatest.')
print('The [2] is removed from the list')
time.sleep(5)
print("Sorted:[2]")
print('unsorted:[7,4,5,7,6,8,3]')
print('We find the smallest number of the unsorted which is [3].')
time.sleep(3)
print("Then we keep on going on and on getting the smallest number of the array")
print("and moving it to the sorted list one element at a time eventually ending when")
print("the unsorted array is then empty.")
time.sleep(5)
print("Sorted:[2,3]")
print('unsorted:[7,4,5,7,6,8]')
time.sleep(1)
print("Sorted:[2,3,4]")
print('unsorted:[7,5,7,6,8]')
time.sleep(1)
print("Sorted:[2,3,4,5]")
print('unsorted:[7,7,6,8]')
time.sleep(1)
print("Sorted:[2,3,4,5,6]")
print('unsorted:[7,7,8]')
time.sleep(1)
print("Sorted:[2,3,4,5,6,7]")
print('unsorted:[7,8]')
time.sleep(1)
print("Sorted:[2,3,4,5,6,7,7]")
print('unsorted:[8]')
time.sleep(1)
print("Sorted:[2,3,4,5,6,7,7,8]")
time.sleep(1)
print("We are sorted and done")
print('Let me show another example!.')


#stopping until user input
#because of different version implementations T.T
#computerlabs at holy building (WMC) uses python 2.x
if sys.version_info <= (3,0):
    raw_input("Press any key to continue.")
else:
    input("Press any key to continue.")
unsortlist=[3,9,5,2,7,7]
#unsortlist=[9,8,7,6,5,4,3,2,1]
x=SelectionSort(unsortlist)
print(x)
#user putting it in
print('Now let us have you put in an array to visualize the algorthim')
print('Please enter numbers only into this query.')
print('After you are done putting the number please put spaces and punctuation between them')
print('To signify you are done with your query')
print('After you are done with the numbers for our array please press "enter"')\
#biggggg string user enters
userstring=input('Please enter numbers here:')
#empty list for integers user puts in
userlist=[]
#regex magic (I dunno how this works google it mate)
regextedstringsofnumbers=re.findall(r"\b[0-9]+\b", userstring)
#forloop of transferance of integers
for x in regextedstringsofnumbers:
    y=int(x)
    userlist.append(y)
#calling the selectionsort
sortlist=SelectionSort(userlist)
#printin'
print(sortlist)
#all the other algo copy this so yeah I was lazy.


