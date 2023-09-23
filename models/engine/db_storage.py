#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """ Defines a database storage engine
        Attributes:
        __engine(sqlalchemy.engine): working sqlalcchemy engine 
        __session(sqlalchemy.session): working sqlalchemy session
    """
    __engine = None
    __session = None
    def __init__(self):
        """ Initialize a dbstorage instance. """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/()".
                                      format(getenv("HBNB_MYSQL_USER"),
                                            (getenv("HBNB_MYSQL_PWD"),
                                            (getenv("HBNB_MYSQL_HOST"),
                                            (getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query all database objects in the session according to class
            If class is None query all types of objects
            Return a dictionary key=<class-name>.<object-id>, value=object
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all()
            objs.extend(self.__session.query(Users).all()
            objs.extend(self.__session.query(Amenity).all()
            objs.extend(self.__session.query(Place).all()
            objs.extend(self.__session.query(Review).all()
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables after importing the Base class, persist the session
            by setting expire_on_commit to false, and use a scoped session to make the
            session thread-safe
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Close the working SQLalchemy session """
        self.__session.close()
