#!/usr/bin/python3
"""
Command interpreter.
Imports
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self):
        """
            do_quit().
            Quit command to exit the program.
        """
        return True

    def do_EOF(self):
        """
            do_EOF()
            Exit the program with Ctrl+D.
        """
        return True

    def emptyline(self) -> bool:
        """
            emptyline()
            When a user enters an empty line,
            this function is called.
        """
        pass
