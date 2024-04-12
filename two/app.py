from models import User
from sqlalchemy.orm import sessionmaker
from db import engine

session = sessionmaker()(bind=engine)

users = session.query(User).all()
# output will be list object of "User"
print(users)

users = session.query(User).first()
# output will be first object in list object of "User"
print(users)


## one() = first() = scalar() but first() is best

users = session.query(User).filter(User.id==4).one()
# output will be spcefic object in list object of "User"
print(users)
users = session.query(User).filter(User.id==4).first()
# output will be spcefic object in list object of "User"
print(users)
users = session.query(User).filter(User.id>4).all()
# output will be spcefic object in list object of "User"
print(users)
users = session.query(User).filter(User.id!=5).all()
# output will be spcefic object in list object of "User"
print(users)


users = session.query(User).count()
# to count the sum of object of "User"
print(users)


users = session.query(User).all()
# output will be last object in list object of "User"
print(users[::-1][0])
print(users[-1])
