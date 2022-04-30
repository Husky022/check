from sqlalchemy import Column, Integer, DateTime, BigInteger, BOOLEAN, String

from database.dbcore import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(BigInteger)
    state = Column(String, default='0')
    subscribe = Column(BOOLEAN, default=False)

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"{self.user_id} - {self.name}"


