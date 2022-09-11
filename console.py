#!/usr/bin/python3
from models.base_model import BaseModel

""" console """
import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    intro = 'Welcome to the hbnb shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit the program"""
        return True

    def do_EOF(self, arg):
        """quit the program"""
        return True

    def emptyline(self):
        """return nothing"""
        return False
    
    def do_create(self, arg):
        """create new base model instance"""
        model = BaseModel()
        print(model)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
