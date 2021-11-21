'''
2. Write a program that creates a new list containing all the elements placed 
on even positions of the original list.
[43, 23, 21, 44, 56, 75] -> [23, 44, 75]
'''



list=[43, 23, 21, 44, 56, 75]
#new list
newlist=[]
for i in range(len(list)): #  len counts the length of a ie 6 an take range upto that 
    #For even position not the index 
    if i%2==1:
        newlist.append(list[i])
print(newlist)
