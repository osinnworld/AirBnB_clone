#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

class BaseModel():
    """
    Parent class for all classes in the AirBnB clone project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes BaseModel attributes.
        """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            self.__load_from_kwargs(kwargs, date_format)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __load_from_kwargs(self, kwargs, date_format):
        """
        Loads attributes from kwargs.
        """
        for key, value in kwargs.items():
            if key == "created_at":
                self.created_at = datetime.strptime(value, date_format)
            elif key == "updated_at":
                self.updated_at = datetime.strptime(value, date_format)
            elif key != "__class__":
                setattr(self, key, value)

    def __str__(self):
        """
        Returns string representation of the object.
        """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """
        Returns string representation of the object.
        """
        return self.__str__()

    def save(self):
        """
        Updates 'updated_at' attribute and saves the object to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary representation of the object.
        """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic

