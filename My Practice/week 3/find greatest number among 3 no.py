'''Write a program that takes 3 numbers as input and
outputs the greater of the 3 numbers'''

#taking input from the user
a=int(input("Enter the first mumber: " ))
b=int(input("Enter the second mumber: " ))
c=int(input("Enter the third mumber: " ))

#using condition
if a>b and a>c:
    print("The greatest number is a")
    
elif b>a and b>c:
    print("The greatest number is b")

else:
    print("The greatest number is c")
