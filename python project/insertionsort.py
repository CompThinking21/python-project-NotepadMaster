from __future__ import print_function
#insertion sort
#for sleep()
import time
#for regexin'
import re

#only accepts arrays (lists)
#this memory complexity O(n)
#time complexity O(n^2)
'''
needed to work on the printing during the algo to truly show what is going on but gave up
'''
def insertionsort(array):
    #going through from 1 (the second item in the array) to length of array
    #this is to make sure that we start by comparing the second item to the first item
    for a in range(1, len(array)):

        #setting key as array[a] to make easier to understand.
        #the key can access what is inside array at the bth element
        keya = array[a]

        #getting the a-1 so the element before element array[a]
        b = a-1

        #WHILE elemint (a-1) is greater or equal to zero True
        #AND keya (array[a]) is less than array[b] is True
        #essentially while array[a] is less than array[b] and b not less than 0
        #or the array has not hit array[-1] do what is indented
        #all of this is possible since lists are mutable (changable)
        while b >=0 and keya < array[b]:
            print('(keya:', keya, end=') < (')
            print('array[b]:', array[b], end=')')
            print('')
            time.sleep(2)
            #shifts the array[b] to the right by one essentially taking the place of array[a].
            #and array[a] taking the place of b but is currently saved in keya while being looped
            #in the while loop as long ad the above conditions are met
            array[b+1] = array[b]
            #when the above conditions are met b=b-1
            #why since array[b] was less than array[a] and array[b] takes the place of array[a] (ath spot of array)
            #it -1 to go check the the next spot
            b-=1
            #then do the while loop again until b= -1 or array[b] < array[a] (keya) which at that point stops
        #once the while conditions are no longer met put the value of keya into array[j+1]
        array[b+1]=keya
        print(array)
        time.sleep(2)

#main
print('This is a sorting method called insertion sort.')
time.sleep(3)
print('This is the second simplest sorting method.')
time.sleep(3)
print('Although it is simple the idea is very convoluted so please pay attention.')
time.sleep(3)
print("The idea of insertion sort is that it's for loop from the second element of array x to the last element of the array.")
print("For every loop it would check element previous to it then shift the larger number the right and move it.")
print("Then it would move the smaller number to the right.")
time.sleep(10)
print("This would keep going until either one of the following occurs.")
print("Also to clarify the element being compare as pivot and the element comparing to it 'comele'.")
time.sleep(5)
print("a) Either the pivot is greater than the 'comele' thence the loop ends and moves on to the next element of the list.")
time.sleep(3)
print("b) Or the pivot has reached the end of the array and is trying to go beyond it at which it stops and replaces")
print("the first element[Which has already shifted to the right].")
time.sleep(7)
print("Did you get it?.")
time.sleep(2)
print("I do not thinks so.")
time.sleep(2)
print("Let me help you see it visually to help you.")
time.sleep(3)
print("I will be using a small list of [3,2,1,4] as an example.")
time.sleep(3)
print("So the first element is already out of the equation and the loop starts from the second element.")
time.sleep(4)
print("I will also make two lists to visuallize it better first list is where the sorted list lie.")
time.sleep(3)
print("The other list is where the unsorted elements are piled for later as we will see even though it shifts and compares")
print("to the right the algorithm is designed to remember which spot they are suppose to be at.")
time.sleep(7)
print("Sorted:[3]")
print("Unsorted:[2,1,4]")
time.sleep(4)
print("Then we move the second element of the unsorted list [2] within the list into the sorted pile.")
print("That [2] is considered the pivot of the explaination above or the number being compared.")
print("Sorted:[3,2]")
print("Unsorted:[1,4]")
print("Pivot: 2")
time.sleep(5)
print("Then we compare the first element and the second element of the of the sorted array.")
print("3<2?")
time.sleep(3)
print("If False then they switch.")
print("Sorted:[2,3]")
print("Unsorted:[1,4]")
print("Pivot: 2")
time.sleep(3)
print("Now that the pivot as arrived at the end of the array it stops and goes to the next element of the unsorted array.")
time.sleep(3)
print("Now we move the third element [1] from the unsorted to the sorted.")
print("Sorted:[2,3,1]")
print("Unsorted:[4]")
print("Pivot: 1")
time.sleep(5)
print("Then we do it all again we check it all again.")
print("3<1?")
time.sleep(3)
print("Sorted:[2,1,3]")
print("Unsorted:[4]")
time.sleep(2)
print("3<1?")
time.sleep(2)
print("Sorted:[1,2,3]")
print("Unsorted:[4]")
time.sleep(3)
print("Then the pivot [1] has reached the end of the array and thus we move to the next and last element.")
time.sleep(3)
print("Same thing")
print("Sorted:[2,3,1,4]")
print("Unsorted:[]")
print("Pivot: 4")
time.sleep(4)
print("4<3?")
print('No?')
time.sleep(3)
print("Skip")
time.sleep(3)
print("This we get a sorted list [1,2,3,4].")
print("Thus we are done.")
time.sleep(3)
#clarifications
print('We will try an example with a list of [7,6,5,4,3,2,1,9,8].')
time.sleep(3)
unsortarray=[7,6,5,4,3,2,1,9,8]
insertionsort(unsortarray)
print(unsortarray)
print('')
print('')
print('')
print('')
print('')
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
#sortin'
insertionsort(userlist)
#done
print(userlist)
time.sleep(15)
