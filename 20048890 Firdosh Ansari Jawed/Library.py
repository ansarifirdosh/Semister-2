
bookList = []
authorList = []
quantityList = []
priceList = []

def getList() -> None: #-> None is an annotation indicating the method
    '''initializes the values of lists by reading the file and using proper data structures'''
    b = open("text/library.txt")
    
    content = [c.strip("\n") for c in b.readlines()]  #read and strip down line breaks, store lines in an array
    b.close()
   
    for i in range(len(content)):
        m = 0
        for c in content[i].split(","):
            if m == 0: 
                bookList.append(c) #2d list 
            elif m == 1:
                authorList.append(c)
            elif m == 2:
                quantityList.append(c)
            elif m == 3:
                priceList.append(c.strip("$")) #remove/strip down $ chars
            m += 1
