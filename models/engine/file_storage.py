#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class manages the storage of objects in a JSON file for the AirBnB clone project.

    Attributes:
        __file_path (str): The path of the JSON file to save objects to.
        __objects (dict): A dictionary mapping object keys to their instances.
        class_dict (dict): A dictionary mapping class names to their corresponding classes.
    """

    __file_path = 'file.json'
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State
    }

    def all(self):
        """
        Returns a dictionary of all objects stored.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object instance to the storage dictionary.

        Args:
            obj: The object instance to be added.
        """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes object instances to JSON and saves them to the file.
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes object dictionaries from the file and converts them back to object instances.
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                class_name = value['__class__']
                obj = self.class_dict[class_name](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass

