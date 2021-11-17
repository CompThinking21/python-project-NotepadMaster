from __future__ import print_function
#for sleep()
import time

#must be arrays (lists) only
def SelectionSort(array):
    #while loop
    sortarray=[]
    while len(array) !=0:
        #getting the pseudosmallest
        smallest=array[0]
        for num in range(1,len(array)):
            if array[num]<smallest:
                smallest=array[num]
        sortarray.append(smallest)
        array.remove(smallest)
        #printing results
        print("the smallest number is", smallest)
        print (sortarray, end='')
        print (array)
        time.sleep(2)
    return sortarray
#main
print("Welcome to Selection Sort module also called bubble sort")
time.sleep(3)
print('What is selection sort? Simple it is the simplest sorting algoeithm known to man')
time.sleep(3)
print('The idea is very simple it is essentially like sorting a hand of cards')
time.sleep(3)
print('It is getting a hand of cards and moving the smallest value to your other hand')
time.sleep(3)
print('You keep on doing this until your original hand has no more cards')
time.sleep(3)
print('Let me show an example!')
#stopping until user input
raw_input("Press any key to continue.")
unsortlist=[3,9,5,2,7,7]
#unsortlist=[9,8,7,6,5,4,3,2,1]
x=SelectionSort(unsortlist)
print(x)
