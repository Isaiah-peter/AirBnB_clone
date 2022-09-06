#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.__dict__["id"])
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            my_dict = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(my_dict, f)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                jb = json.load(f)
                for key in jb:
                    self.__objects[key] = classes[jb[key]
                                                  ["__classes__"]](**jb[key])
        else:
            print("worked")
            return