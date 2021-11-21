'''Write a program that takes two numbers as input and
finds out the GCD (greatest common divisor) of the two
numbers using the Euclidean algorithm. (Use while
loop'''

#taking input from the user
m=int(input("Enter the first number: "))
n=int(input("Enter the second number: "))

if m<n:
    temp=m
    m=n
    n=temp
r=m%n

while(r!=0):
    m=n
    n=r
    r=m%n

print("The greatest common divisor is",n)   
