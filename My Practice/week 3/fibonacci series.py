'''A Fibonacci sequence is characterized by the fact that every number after 
the first two is the sum of the two preceding ones. By definition, the first 
two numbers in the Fibonacci sequence are 1 and 1.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55 …
Write a program that generates the first N numbers of the Fibonacci 
sequence and prints them out. N should be taken as input from the user.
(Use for loop'''
#Taking input from the user

n=int(input("Enter upto which term u want to print fibonacci series: "))

a=0
b=1
if n==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n):
        fibo=a+b
        a=b
        b=fibo
        print(fibo)
        
    




      
