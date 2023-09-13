#!/usr/bin/python3
"""
This module defines a program that contains
the entry point of the command interpreter:
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class definition for the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        method to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        method to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
