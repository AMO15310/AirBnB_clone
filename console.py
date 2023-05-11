#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """
        Quit command to exit the program 
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program 
        """
        print ()
        return True

    def emptyline(self):
        """
        Overriding emptyline method to do nothing when user enters nothing
        """

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()