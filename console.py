#!/usr/bin/python3

"""
Command interpreter.
Imports

"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
storage = FileStorage()


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
            do_create()
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

    def do_show(self, arg):
        """
            do_show()
            Prints the string representation of an instance based
            on the class name and id.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            print(storage.all()[key])

    def do_destroy(self, arg):
        """
            do_destroy()
            Deletes an instance based on the class name and id
            (save the change into the JSON file).
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name.
        """
        args = arg.split()
        if not args:
            instances = storage.all()
            for key, value in instances.items():
                strPrint = str(value)
                print(strPrint)
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instances = storage.all()
            for key, instance in instances.items():
                if key.startswith(class_name + '.'):
                    strPrint = str(instance)
                    print(strPrint)

    def do_update(self, arg):
        """
            Updates an instance based on the class name
            and id by adding or updating attribute.
        """
        args = arg.split()
        className = args[0]
        classID = args[1]
        classAttribute = args[2]
        classValue = args[3]

        print("Args:", args)
        print("ClassName", className)
        print("ClassID", classID)
        print("ClassAttribute", classAttribute)
        print("ClassValue", classValue)

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 4:
            print("** Missing arguments **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
