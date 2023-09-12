TICKETLIST =[]

class Ticket:
    count=101

    def __init__(self , name, author , price):
        self.id=Ticket.count
        self.name=name
        self.author=author
        self.price=price
        Ticket.count =+ 1

    def __str__(self):
        return f"{self.id} Name:{self.name} Authour: {self.author} Price: {self.price}"

def bookTicket():
    origin=input("Enter Book Name :")
    destination=input("Enter author Name")
    date=input("Enter the price")
    ticketdetails = (name, author, price)
    TICKETLIST.append(ticketdetails)

def showAllBooks():
    for book in TICKETLIST:
        print(book)

def DeleteBook():
    id=int(input("Enter the book id"))
    for  book in TICKETLIST:
        if id == book.id:
            TICKETLIST.remove(book)

def main():
    while True:
        print("Choose the option")
        print("1. Add a new Book")
        print("2. Delete a Book")
        print("3. Show all the Books")
        print("4. Exit")

        choice=int(input("Enter your choice :- "))

        if choice == 1:
            addBook()
            print("Book Added Successfully..!")

        elif choice == 2:
            DeleteBook()
            print("Book Delete Successfully..!")
        
        elif choice == 3:
            showAllBooks()

        elif choice == 4:
            print("---End of program---")
            break
        
        else:
            print("Choose the Correct Input")

        print("-----------------------------")

main()