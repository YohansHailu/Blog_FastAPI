from BaseEntity import *

class UserProfile(BaseEntity):
    __tablename__ = "profile"

    userId = Column(Integer, unique=True)
    firstName = Column(String)
    lastName = Column(String)
    bio = Column(String)

    
