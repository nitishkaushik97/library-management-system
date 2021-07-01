class library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        for book in self.books:
            print ' *{}'.format(book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            print 'You have been issued {}. Please keep it safe and return it within 30 days.'.format(bookName)
        else:
            print'Sorry, this book is not available right now. Please try again later.'

    def returnBook(self,bookName):
        self.books.append(bookName)
        print 'Thanks for providing this book! Hope you enjoyed reading it. Have a nice day ahead.'

class Student:
    def requestBook(self):
        self.book = raw_input('Enter the name of the book you want to borrow: ')
        return self.book
    def returnBook(self):
        self.book = raw_input('Enter the name of the book you want to return: ')
        return self.book

if __name__ == '__main__':
    centralLibrary = library(['Math','Science','English','Hindi'])
    student=Student()
    print '\n\t\t===Welcome to Central Library==='
    
    while(True):
        welcomeMsg = '''
\tPlease Choose an option:
\t1. List all books
\t2. Request a book
\t3. Add/Return a book
\t4. Exit the library
'''
        print (welcomeMsg)
        a=input('Enter your choice no.: ')
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print 'Thanks for choosing Central Library.'
            exit()
        else:
            print 'Invalid Choice!'
