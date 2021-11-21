'''
3. Write a program that combines two lists of equal length by alternatingly 
taking elements, e.g. 
[‘a’, ‘b’, ‘c’], [1, 2, 3] -> [‘a’, 1, ‘b’, 2, ‘c’, 3]
'''

lista=['a','b','c'] #initializing first value.
listb=[1,2,3]  #initializing second value.
combo=[]    

for i in range(len(lista)):   #count total number of inputs in a and keep the value in range
    combo.append(lista[i])
    combo.append(listb[i])

print(combo)    
