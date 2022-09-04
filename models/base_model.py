#!/usr/bin/python3
""" Base Class Module """

import uuid
from datetime import datetime


class BaseModel:
    """ Base class"""

    def __init__(self):
        id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()

    def __str__(self):
        """print a base model"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
        of the instance """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
