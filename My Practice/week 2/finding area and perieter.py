'''Write a program that asks the user to input length and breadth of a rectangle.
Then the program should calculate to area and perimeter of the rectangle and
print them out. Area = 𝑙 × 𝑏; Perimeter = 2 𝑙 + 𝑏 ;#'''

#Asking length and breadth
a=float(input("enter the length: "))
b=float(input("enter the breadth: "))

#using formula for area and perimeter of rectangle
area=a*b
peri=2*(a+b)

#printing out the values
print("the area of rectangle is: ",area)
print("the perimeter of rectangle is: ",peri)
