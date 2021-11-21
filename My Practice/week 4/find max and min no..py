'''Write a program that takes N number of integers as input and puts them in 
a list. Then it should find out the maximum and minimum number from the 
list and print them out. The whole list must also be printed out.
(Hint: Assume that the first element of the list is maximum/minimum 
element, then iterate through the list comparing the assumed value with 
every other element to find the maximum and minimum value)'''



a=[]
size=int(input("Enter the size of list: "))   # taking the size of number from user

for i in range(size):
    value=int(input("Please enter the numbers: "))#taking the list of number fr4om user
    a.append(value)

max=a[0]
for i in range(size):
    if(a[i]>max):   #check condition from all the given number and choose the smallest one
        max=a[i]

min=a[0]
for i in range(size):  
    if(a[i]<min):    #check condition from all the given number and choose the smallest one
        min=a[i]

print("The maximum number is: ",max) #print maximum number
print("The minimum number is: ",min) # print minimum number
