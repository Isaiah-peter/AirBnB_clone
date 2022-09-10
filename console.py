#!/usr/bin/python3

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
        """don't run empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
