import Return
import Borrow
import Library as library 

def initialize() -> None: #-> None is an indication the method should always return void
    '''initialize the program'''
    while (True):  #infinite loop
        print(f'''
        Welcome to Islington Library Management System
{"-"*50} 
        Enter 1 to display
        Enter 2 to borrow a book
        Enter 3 to return a book
        Enter 4 to exit
{"-"*80} 
        ''')

        try:
            want = int(input("Please select a number from 1 to 4: "))
            if (want == 1):
                b = open("text/library.txt")#opens the book available in library
                print("-------Here is the list of books------------.  \n")
                print(" Name of Book,Author,Quantity,price")
                print(b.read() + " \n Four books are displayed above. \n")
                b.close()
            elif (want == 2):
                library.getList()  #initialize values of lists of books to borrow
                Borrow.borrowBook()
            elif (want == 3):
                library.getList()  #initialize values of lists of book to return
                Return.returnBook()
            elif (want == 4):
                print("Thank you visit again")
                break  #get out of loop
            else:
                print("Invalid input. Please check and try again.")
        except ValueError as error:  #if input can not be parsed
            print(f"Please input a valid number. {error}")

        

#initialize the program
initialize()
