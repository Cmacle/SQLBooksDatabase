from sqlalchemy import (create_engine, Column,
                         Integer, String, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import BLOB, Float, Date


engine = create_engine('sqlite:///books.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column('Title', String)
    author = Column('Author', String)
    published_date = Column('Published', Date)
    price = Column('Price', Float)
    file = Column('File', BLOB)
    file_name = Column('File Name', String)
    file_type = Column('File Type', String)
    file_size = Column('File Size', Float)
    

    def __repr__(self):
        return f'ID= {self.id},Title= {self.title},Author= {self.author},Published= {self.published_date},Price= {self.price},File Type= {self.file_type},File Size= {self.file_size}'