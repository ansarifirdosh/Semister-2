'''Write a program that asks the user to enter the name of a student and 
marks obtained in any 5 subjects of your choice. The program should 
calculate the average marks obtained by the student and assign the overall 
grade according to the following criteria:
70 – 100 A
60 – 69 B
50 – 59 C
43 – 49 D
40 – 42 E
0 – 39 F
The output of the program should include the name of the student, the 
marks obtained in the 5 subjects, the average marks and the overall grade.'''

#Taking input from the user
name=input("Enter the Name of student: ")
sci=float(input("Enter the marks in Science: "))
math=float(input("Enter the marks in Maths: "))
nep=float(input("Enter the marks in nepali: "))
comp=float(input("Enter the marks in computer: "))
eng=float(input("Enter the marks in English: "))

Total=sci+math+nep+comp+eng
avg=Total/5

print("-----------The result is here-------------")
print("The name of student is: ",name)
print("The total marks is: ",Total)
print(name+"'s Average mark is: ",avg)

if avg>=70 and avg<=100:
    print("Grade A")
elif avg>=60 and avg<=69:
    print("grade B")
elif avg>=50 and avg<=59:
    print("grade c")
elif avg>=43 and avg<=49:
    print("grade d")
elif avg>=40 and avg<=42:
    print("grade E")
elif avg>=0 and avg<=39:
    print("you are fail")
else:
    print("please enter the valid marks")
    
