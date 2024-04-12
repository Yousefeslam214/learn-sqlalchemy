import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import pymysql

# ROOT_PATH = os.path.dirname(os.path.realpath(__file__));
# DB_URI = os.path.join(ROOT_PATH, 'db.db')
# engine = create_engine(f"sqlite:///{DB_URI}", echo=True);


db_user = "root";
db_pass = "";
db_host = "127.0.0.1";
db_name = "sqlalchemy_tutorial";

engine = create_engine(f'mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}', echo=True)

Base = declarative_base()

# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer(), primary_key=True);
#     name = Column(String(111), nullable=False);

# Base.metadata.create_all(bind=engine);
