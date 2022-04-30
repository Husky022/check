from datetime import datetime
from os import path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.dbcore import Base

from settings import configuration

from models.users import User


class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singleton):
    def __init__(self):
        self.engine = create_engine(configuration.DATABASE)
        session = sessionmaker(bind=self.engine)
        self.session = session()
        print(path.isfile(configuration.DATABASE))
        if not path.isfile(configuration.DATABASE):
            Base.metadata.create_all(self.engine)

    def close(self):
        self.session.close()

    def commit(self):
        self.session.commit()

    def add_new_user(self, user_id, name):
        current_user = self.session.query(User).filter_by(user_id=user_id)
        if not current_user:
            new_user = User(user_id, name)
            self.session.add(new_user)
            self.commit()
            self.close()

    def set_user_state(self, user_id, state):
        current_user = self.session.query(User).filter_by(user_id=user_id).first()
        current_user.state = state
        self.commit()
        self.close()

    def get_user_state(self, user_id):
        current_user = self.session.query(User).filter_by(user_id=user_id).first()
        state = current_user.state
        self.close()
        return state
