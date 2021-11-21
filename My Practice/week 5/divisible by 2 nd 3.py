'''
1. Write a program that prints out all the elements of a list which are divisible 
by 2 and 3. Use the following list,
a = [2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112]
'''

list=[2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112]

for i in range(len(list)):#The len function returns the number of items in an object.
    
    if list[i]%2==0 and list[i]%3==0:  #USING IF Condition
        
        print("The number which are divisible by 2 and 3 are: ",list[i])
        
