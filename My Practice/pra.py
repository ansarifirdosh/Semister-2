student={}
n=int(input("Enter the number of students: "))
for i in range(n):
       name=input("Enter the name of student: ")
       marks=[]
       n1=int(input("Enter the number of subject: "))
       for i in range(n1):
           m=int(input("Enter the marks: "))
           marks.append(m)
student[name]=marks    
             
print(student)      

for i in student:
    print('Student name',i,end='')
    total_marks=sum(student[i])
    percentage=total_marks/n1
    div=''
    if percentage>=60:
        div='first position'
    elif percentage>=50:
        div='second position'
    elif percentage>=40:
        div='third position'
    elif percentage>=30:
        div='pass'
    else:
        div='fail'
        
        
print(' your total marks: ',total_marks,'and percentage is ',percentage,div)    
    
     
    
       

    
