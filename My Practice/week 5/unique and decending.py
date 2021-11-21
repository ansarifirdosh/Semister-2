'''
1. Write a program that creates a new list containing only the unique elements 
from the original list in descending order. 
[1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6] -> [6, 5, 4, 3, 2, 1]
'''


l=[1,1,2,3,3,4,4,5,6,5,6]
u=[]
a=len(l)  #count the number in l
for i in l:
    if i not in u:
        u.append(i)
print(u)

u.sort(reverse=True)

print("decending order is:",u)
