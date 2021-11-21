''' Write a program that asks the user to enter two numbers a and b. Then 
write code to swap the values of a and b, and print them out'''

#taking input from the user
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

#printing code before swap
print("The value of a and b before swapping: ")
print(a)
print(b)

#code for swapping by putting sad variable
sad=a
a=b
b=sad

#printing values after swap
print("the value of a and b after swap is: ")
print(a)
print(b)
