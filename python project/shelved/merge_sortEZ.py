#originally suppose to demonstrate the mergestep by have insertion sort 2 halves of an array
#then mergining it into a sorted array
#insertion sort

#only accepts arrays (lists)
#this memory complexity O(n)
#time complexity O(n^2)
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
def merge(array1, array2):
    while array1 is not empty and array2 is not empty:
        if array1[a]>=array2[b]:

#main
unsortarray=[7,6,5,4,3,2,1]
insertionsort(unsortarray)
print(unsortarray)
