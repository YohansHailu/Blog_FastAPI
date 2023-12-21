from BaseEntity import *

class User(BaseEntity):
    __tablename__ = "user"

    userName = Column(String, unique=True)
    email = Column(String, unique=True)
