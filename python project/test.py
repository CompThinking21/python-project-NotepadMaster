#test of code.
#importing regex
import re

print('Now let us have you put in a array to visualize the algorthim')
print('Please enter numbers only into this query.')
print('After you are done putting the number please put spaces between them')
print('To signify you are done with your query')
print('After you are done with the numbers for our array please press "enter"')
userstring=input('Please enter numbers here:')
userlist=[]
regextedstringsofnumbers=re.findall(r"\b[0-9]+\b", userstring)
for x in regextedstringsofnumbers:
    y=int(x)
    userlist.append(y)
print(userlist)
    
