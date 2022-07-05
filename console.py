#!/usr/bin/python3
""" Program called console.py that
contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Class definition  """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Use quit to exit of the console """
        return True

    def do_EOF(self, args):
        """ Exit of the console """
        return True

    def do_help(self, args):
        """ Shows the commands of the console """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """ Empty line does not execute anything """
        return False

    def do_create(self, args):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel """

    def do_show(self, args):
        """ Prints the string representation of
        an instance based on the class name and id """

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """

    def do_all(self, args):
        """ Prints all string representation of
        all instances based or not on the class name """

    def do_update(self, args):
        """ Updates an instance based on the class
        name and id by adding or updating attribute """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
