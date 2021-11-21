import DateTime as dtime
import Library as library

def returnBook() -> None: #-> None is an annotation indicating the method should always return void, doesn't affect anything
    '''Handles operations for returning book'''
    count_ = 1
    name = input("please Enter your first name: ")
    borrowRecord = f"text/Borrowed-{name}.txt"
    try: 
        b = open(borrowRecord) #opens in read mode by default        
        data = b.read()
        print(data)
        b.close()
    except:
        print("Please enter correct name and try")
        return #end method, return None

    returnRecord = f"text/Return-{name}.txt"
    borrowRecord = f"text/Borrowed-{name}.txt"
    b = open(returnRecord, "w+")
    b.write(f'''

            Islington Library Management System: \n\n\n
            Returned by: {name} 
            Date: {dtime.getCurrentDate()}
            Time: {dtime.getCurrentTime()}
            \n\tS.N.\t\tBook Name\t\t\tAuthor\t\t\t\tCost\n''')
    b.close()

    total = 0.0
    for i in range(4):
        book = library.bookList[i]
        if book in data:
            b = open(returnRecord, "a") #open in append mode
            b.write(f"\t{count_} \t\t{book}\t\t\t{library.authorList[i]}\t\t\t{library.priceList[i]}\n")
            count_ += 1
            b.close()
            total += float(library.priceList[i])

            b = open(borrowRecord)  #open in read mode
            library.quantityList[i] = int(library.quantityList[i]) + b.read().count(book)  #get how many times this string has repeated in file
            b.close()
            
    
    days = int(input(("How many days ago did you borrowed the book?: ")))
    if (days > 10):
        charge = 7 * (days - 10)
        b = open(returnRecord, "a")
        b.write(f"\t\t\t\t\t\t\t\t\t\tcharge: ${charge}\n")
        b.close()
        total = total + charge
        
    print(f"Final Total: ${total}")

    b = open(returnRecord, "a")
    b.write(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\ttotal: ${total}")
    b.close()

    b = open("text/library.txt", "w+")
    for i in range(3):
        #writing new data to library record file
        b.write(f"{library.bookList[i]},{library.authorList[i]},{str(library.quantityList[i])},${library.priceList[i]}\n")
    b.close()
