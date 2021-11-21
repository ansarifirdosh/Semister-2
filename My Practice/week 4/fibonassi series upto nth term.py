'''
A Fibonacci sequence is characterized by the fact that every number after 
the first two is the sum of the two preceding ones. By definition, the first 
two numbers in the Fibonacci sequence are 1 and 1.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55
Write a program that generates the first N numbers of the Fibonacci 
sequence and prints them out. N should be taken as input from the user.
(Use lists)
'''



nterms = int(input("Enter upto how many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
