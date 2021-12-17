from models import(Base, session, 
                    Book, engine)

def menu():
    
    print('''\nChoose an option: 
            \r1: Add book
            \r2: Search 
            \r3: Analysis 
            \r4: View all books
            \r5: Exit
            ''')
    return input("")

def add():
    pass
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