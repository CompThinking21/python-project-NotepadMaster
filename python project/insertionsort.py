#insertion sort can only accept numlist
def InsertionSort(numlist):
    #a for loop to iterate through all values stored in the list
    #but from the range of that start from the second element
##    for x in range(1, len(numlist)):
##        keya = numlist[x]
##        
##        keyb=keya-1
##        while (keyb>=0) and (keya<numlist[keyb]):
##            numlist[keyb+1] = numlist[keyb]
##            keyb = keyb-1
##
##        numlist[keyb+1] = keya
    #tried to be fancy but heck that
 
        
'''
Psudocode I got from "https://www.cs.mcgill.ca/~cs203/lectures/lecture7/sld005.htm"

'''

#main
unsortlist=[3,9,5,2,7,7]
#unsortlist=[9,8,7,6,5,4,3,2,1]
InsertionSort(unsortlist)
print(unsortlist)
