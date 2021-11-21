'''
2. Write a program that creates a 2D list having m number of rows and n 
number of columns. All elements in the diagonal should be 1, the elements 
above the diagonal should be 2 and the elements below the diagonal should 
be 3. Values for m and n should be taken from the user.
'''
m=int(input("Enter number of rows : "))
n=int(input("Enter number of column : "))

matrix=[]
for i in range(m):
    new_list=[]
    for j in range(n):
        if i==j:
            new_list.append(1)
        elif i<j:
            new_list.append(2)
        else:
            new_list.append(3)
    matrix.append(new_list)
print(matrix)
