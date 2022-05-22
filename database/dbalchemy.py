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
        self.engine = create_engine(configuration.DATABASE, connect_args={'check_same_thread': False})
        session = sessionmaker(bind=self.engine)
        self.session = session()
        if not path.isfile(configuration.DATABASE):
            Base.metadata.create_all(self.engine)

    def close(self):
        self.session.close()

    def commit(self):
        self.session.commit()

    def choose_user(self, message):
        current_user = self.session.query(User).filter_by(user_id=message.from_user.id).first()
        if not current_user:
            self.add_new_user(message.from_user)
            return self.session.query(User).filter_by(user_id=message.from_user.id).first()
        return current_user


    def add_new_user(self, user):
        new_user = User(user.id, user.first_name, user.username)
        self.session.add(new_user)
        self.commit()
        self.close()


    def set_user_state(self, message, state):
        current_user = self.choose_user(message)
        current_user.state = state
        self.commit()
        self.close()


    def get_user_state(self, message):
        current_user = self.choose_user(message)
        state = current_user.state
        self.close()
        return state

    def reset_user_data(self, message):
        current_user = self.choose_user(message)
        current_user.state = '0'
        current_user.cache = {}
        self.commit()
        self.close()

    def set_user_cache(self, message, data):
        current_user = self.choose_user(message)
        current_user.cache = data
        self.commit()
        self.close()

    def get_user_cache(self, message):
        current_user = self.choose_user(message)
        cache = current_user.cache
        self.close()
        return cache

