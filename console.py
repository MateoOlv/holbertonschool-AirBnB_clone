#!/usr/bin/python3
"""
Command interpreter.
Imports
"""
import cmd
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ HBNB command """
    prompt = '(hbnb) '
    classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]
    messagesValues = {
        'missingClass': '** class name missing **',
        'missingValue': '** value missing **',
        'missingID': '** instance id missing **',
        'missingAttribute': '** attribute name missing **',
        'dontExistsClass': "** class doesn't exist **",
        'dontExistsID': '** no instance found **',
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
            do_create()
            Creates a new instance of BaseModel, saves it (to the JSON file).
        """
        if not arg:
            print(self.messagesValues['missingClass'])
        elif arg not in self.classes:
            print(self.messagesValues['dontExistsClass'])
        else:
            objClassName = globals().get(arg)
            instance = objClassName()
            storage.new(instance)
            storage.save()
            print(instance.id)

    def do_show(self, arg):
        """
            do_show()
            Prints the string representation of an instance based
            on the class name and id.
        """
        args = split(arg)
        if not arg:
            print(self.messagesValues['missingClass'])
        elif args[0] not in self.classes:
            print(self.messagesValues['dontExistsClass'])
        elif len(args) < 2:
            print(self.messagesValues['missingID'])
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print(self.messagesValues['dontExistsID'])
            print(storage.all()[key])

    def do_destroy(self, arg):
        """
            do_destroy()
            Deletes an instance based on the class name and id
            (save the change into the JSON file).
        """
        args = split(arg)
        if not arg:
            print(self.messagesValues['missingClass'])
        elif args[0] not in self.classes:
            print(self.messagesValues['dontExistsClass'])
        elif len(args) < 2:
            print(self.messagesValues['missingID'])
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print(self.messagesValues['dontExistsID'])
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name.
        """
        args = split(arg)
        if not args:
            instances = storage.all()
            for key, value in instances.items():
                strPrint = str(value)
                print(strPrint)
        elif args[0] not in self.classes:
            print(self.messagesValues['dontExistsClass'])
        else:
            instances = storage.all()
            for i in [str(instance) for key, instance in instances.items()]:
                print(i)

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by
            adding or updating attribute saved the change into the JSON file.
        """
        args = arg.split()
        if not arg:
            print(self.messagesValues['missingClass'])
        elif args[0] not in self.classes:
            print(self.messagesValues['dontExistsClass'])
        elif len(args) == 1:
            print(self.messagesValues['missingID'])
        elif len(args) == 2:
            print(self.messagesValues['missingAttribute'])
        elif len(args) == 3:
            print(self.messagesValues['missingValue'])
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all():
                print(self.messagesValues['dontExistsID'])
            else:
                objectAttribute = storage.all()[key]
                setattr(objectAttribute, attribute_name, attribute_value)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
