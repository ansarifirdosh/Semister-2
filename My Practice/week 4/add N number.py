'''1.Write a program that takes a number N as input and prints the sum of all the
numbers'''

num=int(input("Enter the range of number: "))

sum=0 #initializing the value
for i in range(1,num+1):
    sum=sum+i

print("the total sum is: ",sum)



#while loop
num=int(input("Enter the range of number: "))
sum=0
i=1
while i<=num:
    sum=sum+i
    i=i+1
print("the sum is: ",sum)    
