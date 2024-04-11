from db import Base, engine
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import pymysql

class User(Base):
    __tablename__ = "usersS";
    id = Column(Integer(), primary_key=True);
    name = Column(String(111), nullable=False);

    def __repr__(self) -> str:
        return f"<{self.id} : {self.name}>"
        return print(f"{self.id} : {self.name}")

Base.metadata.create_all(bind=engine);
