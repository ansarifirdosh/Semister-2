import DateTime as dtime
import Library as library 

def borrowBook() -> None: 
    firstName = input("Enter your first name: ") #taking first name as input from user
    lastName = input("Enter your last name: ") #taking second name as input from user

    borrowRecord = f"text/Borrowed-{firstName}.txt"  #locating borrow record text file
   
    b = open(borrowRecord, "w+")
    b.write(f'''  \n Islington Library Management System: \n\n\n
Borrowed by: {firstName} {lastName} 
Date: {dtime.getCurrentDate()}
Time: {dtime.getCurrentTime()}
\n\tS.N.\t\tBook Name\t\t\tAuthor\t\t\t\tprice\n''')
    b.close()
    
    count = 1
    while True:  #loop until finish
        print("Please select your choice: ")
        print("                           Name of books")
        print("                          ------------------- ")
        [print(f"Enter {i} to borrow book    {library.bookList[i]}") for i in range(len(library.bookList))]

        try:
            index = int(input("Please input book number: "))
            try:  #can throw index out of bounds exception
                if int(library.quantityList[index]) > 0:
                    print("Book is available.Thank you for borrowing")
                    b = open(borrowRecord, "a")  
                    b.write(f"\t{count} \t\t{library.bookList[index]}\t\t\t{library.authorList[index]}\t\t\t{library.priceList[index]}\n")
                    b.close()

                    library.quantityList[index] = int(library.quantityList[index]) - 1
                    b = open("text/library.txt", "w+")
                    for i in range(4):
                        b.write(f"{library.bookList[i]},{library.authorList[i]},{library.quantityList[i]},${library.priceList[i]}\n")
                    b.close()
                    yn = input("Do you want to borrow more books?(yes/no): ")
                    if yn.lower() != "yes":
                        break  #end loop
                    count += 1
                else:
                    print("Book is not available in stock")
                    borrowBook()
            except IndexError:
                print("Please choose book as per their number.")
        except ValueError as err:
            print("Please choose as suggested.")
