# ********************************** assignment 6 **************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/64-Day-64-Exercise-6/.tutorial/Tutorial.md

'''
Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!
'''

# 2 variables: no_of_books - int, books - list
# method to check whether no of books == len of books. will tell error if they r not same.
# we can make 2-3 libraries lib 1, 2, 3...
# books jo hmne enter kri hai kya wo memory main rehti hai ya ni.???
'''
class Library:
    no_of_books = 0
    books = []
    def __init__(self, no_of_books, books):
        self.no_of_books = self.no_of_books + no_of_books
        self.books = self.books + books

    def noOfBooks(self):
        print(f"no of books: {self.no_of_books} and len of books: {len(self.books)}")
        if self.no_of_books == len(self.books):
            print("Records are correct! ")
        else:
            print("Sorry!, records differ! ")

lib1 = Library(1, ["Book1"])
lib2 = Library(2, ["Book2", "Book3"])

lib1.noOfBooks()
lib2.noOfBooks()

# no! the books which we have entered are not stored in memory permanently i.e., they r not persistent.
'''

class Library:
    def __init__(self):
        self.no_of_books = 0#instance variables.
        self.books = []

    def addBooks(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f"No of books: {self.no_of_books} and they are: ")
        for book in self.books:
            print(book)

lib = Library()
lib.addBooks("HP")
lib.showInfo()
lib.addBooks("HP1")
lib.showInfo()