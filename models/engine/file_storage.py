#!/usr/bin/python3
"""Module for FileStorage class."""
import json
import os


class FileStorage:
    """ Class that serializes and deserializes JSON objects """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns the dictionary __objects """
        return FileStorage.__objects
    
    def delete(self, obj=None):
        """deletes obj from __objects if it's inside
        Args:
            obj: given object
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        if obj:
            del self.__objects[key]

    def new(self, obj):
        """  deletes obj from __objects if it’s inside - if obj is equal to None """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        if obj:
            del self.__objects[key]

    def save(self):
        """ Serializes __objects to the JSON file """
        o_dict = {}

        for key, value in FileStorage.__objects.items():
            o_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(o_dict, f)

    def reload(self):
        """ Deserializes __objects from the JSON file """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes_dct = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(classes_dct[value['__class__']](**value))
