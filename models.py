from sqlalchemy import (create_engine, Column,
                         Integer, String, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Float


engine = create_engine('sqlite:///books.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column('Title', String)
    author = Column('Author', String)
    published_date = ('Published', Date)
    price = Column('Price', Float)

    def __repr__(self):
        return f'ID= {self.id},Title= {self.title},Author= {self.author},Published= {self.published_date},Price= {self.price}'