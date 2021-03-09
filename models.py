import os
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import controller
from controller import data_folder
from platform import system



try:
    os.mkdir(os.path.join(controller.data_folder))
except FileExistsError:
    pass



if system() == "Darwin":
    engine = create_engine(f"sqlite:////{data_folder}/data.db")
else:
    engine = create_engine(f"sqlite:///{data_folder}/data.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Report(Base):
    __tablename__ = "report"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    email = Column(String(100))
    phone = Column(String(30))
    website = Column(String(200))
    fb_page = Column(String(200))
    address = Column(String(200))
    state = Column(String(50))
    city = Column(String(50))
    open_hours = Column(String(100))
    search_keyword = Column(String(200))
    source = Column(String(100))


class YelpResults(Base):
    __tablename__ = "yelp"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    reviews = Column(Integer)
    verfied_license = Column(Integer)
    search_keyword = Column(String(200))
    page = Column(Integer)

class YellowPagesResults(Base):
    __tablename__ = "yellowpages"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    reviews = Column(Integer)
    verfied_license = Column(Integer)
    category = Column(String(200))
    years_in_business = Column(String(200))
    search_keyword = Column(String(200))
    page = Column(Integer)


class FacebookPages(Base):
    __tablename__ = "facebook"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    url = Column(String(300))





Base.metadata.create_all(bind=engine)



