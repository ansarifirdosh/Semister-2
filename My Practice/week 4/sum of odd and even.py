'''
1.Write a program that takes N numbers as input from a user and puts them in a list.
Then the program should find out the sum of all the odd numbers and the sum of all
the even numbers from the list.
'''
'''
l=[]
evensum=0
oddsum=0

for i in range(5):  #using for loop statement upto range 5
    l.append(int(input("Please enter the number: ")))#The append() method in python adds a single item to the existing list. It doesn't return a new list of items.
    if l[i]%2==0:  #using if statement to filter the even number
        evensum=evensum+l[i]
    else:
        oddsum=oddsum+l[i]

print("sum of even number is: ",evensum) #print total sum of even number
print("sum of odd number is: ",oddsum)   #print total sum of odd number
'''

#nextmethod


evensum=oddsum=0
num=int(input("Enter number of terms: "))

for i in range(1,num+1):
    if i%2==0:
        evensum=evensum+i
    else:
         oddsum=oddsum+i


print("sum of even number is: ",evensum) #print total sum of even number
print("sum of odd number is: ",oddsum)   #print total sum of odd number         
