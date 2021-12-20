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
    if input("\nUse this to add a new book to the database.\n Would you like to continue? y/n   ").lower() == 'y':
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
            '''
    )
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
        pass
    elif answer == '3':
        pass
    elif answer == '4':
        pass
    elif answer == '5':
        pass
    else:
        print("Invalid Input")
    
def delete_book():
    pass

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