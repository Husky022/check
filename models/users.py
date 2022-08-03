from sqlalchemy import Column, Integer, DateTime, BigInteger, BOOLEAN, String

from sqlalchemy_utils import JSONType

from database.dbcore import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    is_admin = Column(BOOLEAN, default=False)
    username = Column(String)
    name = Column(String)
    user_id = Column(BigInteger)
    chat_id = Column(BigInteger)
    state = Column(String, default='0')
    cache = Column(JSONType)
    subscribe = Column(Integer, default=0)

    def __init__(self, user_id, name, username, chat_id):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.chat_id = chat_id

    def __str__(self):
        return f"{self.user_id} - {self.name}/{self.username}"


