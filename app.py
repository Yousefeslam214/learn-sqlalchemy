from models import User
from sqlalchemy.orm import sessionmaker
from db import engine

session = sessionmaker()(bind=engine)

    #### 3 methods to add date ###
### new_user = User(name='yousef')
### session.add(new_user)
### session.commit()
##
### user_three = User(name='yousef')
### user_four = User(name='yousef')
### user_five = User(name='yousef')
### session.add_all([user_three, user_four, user_five])
### session.commit()
##
##
### users = [
###     User(name='yousef'),
###     User(name='mahmoud'),
###     User(name='hassan')
### ]
### for user in users:
###     session.add(user)
###     session.commit()


    ## How to show data ##
# print("##################")
# users = session.query(User).all()
# print(users)# data represent as a object to fix it got to class user and make __repr__ function
# for user in users:
#     print(f"{user.id} : {user.name}")
# print("##################")
# users = session.query(User).filter(User.id == 8).first()
# print(users)
# print("##################")

    ## update data ##
# update_user = session.query(User).filter(User.id == 9).first()
# print(update_user)
# update_user.name = "masr";
# print(update_user)
# print("##################")

## delete User ##
# delete_user = session.query(User).filter(User.name == "yousef").second()
# session.delete(delete_user)
# session.commit()
