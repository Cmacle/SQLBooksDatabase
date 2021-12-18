from models import(Base, session, 
                    Book, engine)
import csv
import datetime

def menu():
    
    print('''\nChoose an option: 
            \r1: Add book
            \r2: Search 
            \r3: Analysis 
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
        
def add():
    if input("\nUse this to add a new book to the database.\n Would you like to continue? y/n   ").lower() == 'y':
        new_book = Book()
        new_book.title = input("What is the title of the book?:    ")
        new_book.author = input("Who is the author of the book?:    ")
        while True:
            date_str = input("When was the book published? format m/d/y ex.4/5/2000  :   ")
            try:
                new_book.published_date = datetime.datetime.strptime(date_str, "%m/%d/%Y")
            except ValueError:
                print("Invalid Input")
            else:
                break


def search():
    pass
def analysis():
    pass
def view():
    pass



if __name__ == '__main__':
    Base.metadata.create_all(engine)


    while True:
        

        answer = menu()
        if answer == '1':
            add()
        elif answer == '2':
            search()
        elif answer == '3':
            analysis()
        elif answer == '4':
            view()
        elif answer == '5':
            print('Thank you for using the program!')
            break
        else:
            print("Invalid input try again. A number 1-5")