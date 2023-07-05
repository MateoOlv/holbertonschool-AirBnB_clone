#!/usr/bin/python3

"""
Command interpreter.
Imports

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNB command """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
            do_quit().
            Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
            do_EOF()
            Exit the program with Ctrl+D.
        """
        return True

    def emptyline(self):
        """
            emptyline()
            When a user enters an empty line,
            this function is called.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
