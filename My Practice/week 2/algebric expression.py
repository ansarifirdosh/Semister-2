'''Write a program that computes the value of the algebraic 
expression given below. The program should ask the user to input 
the values of x and y. Write comments to describe your code.'''

#taking the value of x and y from user
x=float(input("Enter the value of x: "))
y=float(input("Enter the value of y: "))

#writing algebric equation to put the values of x and y
result=x**3+3*x**2*y+3*x*y**2+y**3

#printing result
print(result)
