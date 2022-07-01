#!/usr/bin/python3
""" Program called console.py that
contains the entry point of the command interpreter 
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """ Class definition  """
    
    prompt = "(hbnb)"

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
