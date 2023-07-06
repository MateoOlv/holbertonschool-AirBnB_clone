#!/usr/bin/python3

"""
Command interpreter.
Imports

"""
import cmd
import json
from models.engine.file_storage import FileStorage
storage = FileStorage()

""" Classes """
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ HBNB command """
    prompt = '(hbnb) '
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

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

    def do_create(self, arg):
        """
            to_create()
            Creates a new instance of BaseModel, saves it (to the JSON file).
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            objClassName = globals().get(arg)
            instance = objClassName()
            storage.new(instance)
            storage.save()
            print(instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
