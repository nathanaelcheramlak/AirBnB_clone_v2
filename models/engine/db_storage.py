#!/usr/bin/python3
"""Module for DBStorage using sqlAlchemy"""
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        environ = getenv("HBNB_ENV")

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{passwd}\
                                      @{host}/{db}', pool_pre_ping=True)

        if environ == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        query_dict = {}
        if not cls:
            class_ls = ["User", "State", "City", "Amenity", "Place", "Review"]

            for cl in class_ls:
                query = self.__session.query(cl)
                for elem in query:
                    key = f'{type(elem).__name__}.{elem.id}'
                    query_dict[key] = elem

        else:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = f'{type(elem).__name__}.{elem.id}'
                query_dict[key] = elem

        return query_dict

    def new(self, obj):
        """Adds a new element in the table"""
        self.__session.add(obj)

    def save(self):
        """Saves all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an element in the tabele"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Configuration"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()
