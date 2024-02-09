#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """
    A base model class representing a generic data model.

    Attributes:
        id (str): A unique identifier for the model instance.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Converts the instance attributes into a dictionary representation.

        Returns:
            dict: A dictionary containing the instance attributes.
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My Base Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
