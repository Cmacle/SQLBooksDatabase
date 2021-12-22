from models import(Base, session, 
                    Book, engine)
import csv
import datetime

def menu(): 
    print('''\nChoose an option: 
            \r1: Add book
            \r2: Search 
            \r3: Delete 
            \r4: View all books
            \r5: Exit
            ''')
    return input("")

def clean_date(date_str):
    return datetime.datetime.strptime(date_str, '%B %d, %Y').date()

def clean_price(price_str):
    return float(price_str)
    
def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            title = row[0]
            author = row[1]
            date = clean_date(row[2])
            price = clean_price(row[3])
            new_book = Book(title=title, author=author, published_date=date, price=price)
            session.add(new_book)
        session.commit()

def print_ids():
    books = session.query(Book).all()
    ids = [str(book.id) for book in books]
    print(ids)
    return ids
        
def add_book():
    new_book = Book()
    new_book.title = input("What is the title of the book?:    ")
    new_book.author = input("Who is the author of the book?:    ")
    while True:
        date_str = input("When was the book published? format m/d/y ex.4/5/2000  :   ")
        try:
            new_book.published_date = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
        except ValueError:
            print("Invalid Input")
        else:
            break
    while True:
        try:
            new_book.price = float(input("What is the cost? No special characters. ex) 29.99:     "))
        except TypeError:
            print("Invalid Input")
        else:
            break
    print(new_book)
    if input("Do you want to add this book?  y/n     ").lower() == 'y':
        session.add(new_book)
        session.commit()
    else:
        print("Book not added")    
        
def search_book():
    print('''\nWhat would you like to search by?
            \r1: ID
            \r2: Title
            \r3: Author
            \r4: Date Published
            \r5: Price
            ''')
    answer = input("")
    if answer == '1':
        ids = print_ids()
        answer = input('Choose an ID from the list:   ')
        if answer in ids:
            book = session.query(Book).filter_by(id=answer).one()
            print(book)
        else:
            print('ID Not Found')  
    elif answer == '2':
        answer = input("What title would you like to search for?:    ")
        books = session.query(Book).filter_by(title=answer).all()
        if(books):
            for book in books:
                print(book)
        else:
            print("Book not found")   
    elif answer == '3':
        answer = input("What author would you like to search for?:    ")
        books = session.query(Book).filter_by(author=answer).all()
        if(books):
            for book in books:
                print(book)
        else:
            print("Author not found")
        pass
    elif answer == '4':
        answer = input("What date would you like to search? format m/d/y :     ")
        try:
            date = datetime.datetime.strptime(answer, "%m/%d/%Y").date()
        except ValueError:
            print("Invalid Input")
        else:
            books = session.query(Book).filter_by(published_date=date).all()
            if books:
                for book in books:
                    print(book)
            else:
                print("Date not found")
    elif answer == '5':
        answer = input("Input the price of the book without special characters:    ")
        try:
            answer = float(answer)
        except ValueError:
            print("Invalid Input")
        else:
            books = session.query(Book).filter_by(price=answer).all()
            if books:
                for book in books:
                    print(book)
            else:
                print("There is no book for that price.")   
    else:
        print("Invalid Input")
    
def delete_book():
    print('This will permanently delete a book from the database.')
    ids = print_ids()
    answer = input('Choose an ID from the list to be deleted:    ')
    if answer in ids:
        book = session.query(Book).filter_by(id=answer).one()
        print(book)
        if input('Are you sure you would like to delete this book? y/n:    ').lower() == 'y':
            session.delete(book)
            session.commit()
            print('Book Deleted')
        else:
            print("Deletion Aborted")
    else:
        print('''\nThat ID does not exist.
                \rtip: Use the search function to find the ID
                \rof the book you'd like to delete.''')

def view_book():
    for book in session.query(Book):
        print(f'{book.id}) Title = {book.title} Author = {book.author} Published = {book.published_date} Price = {book.price}')
    
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    while True:
        answer = menu()
        if answer == '1':
            add_book()
        elif answer == '2':
            search_book()
        elif answer == '3':
            delete_book()
        elif answer == '4':
            view_book()
        elif answer == '5':
            print('Thank you for using the program!')
            break
        else:
            print("Invalid input try again. A number 1-5")