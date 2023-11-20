#!/usr/bin/python3
""" Module for HBNBCommand """
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand processor"""

    prompt = "(hbnb) "
    class_list = ['BaseModel',
                  'User', 'State',
                  'City', 'Amenity',
                  'Place', 'Review']

    def do_EOF(self, line):
        """Handles End Of File character."""
        print()
        return True

    def do_quit(self, line):
        """Quits the program."""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it
        Exceptions:
            SyntaxError: when ther is no arguments given
            NameError: where there is no name for the object
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            dict_obj = eval("{}()".format(my_list[0]))
            print("{}".format(dict_obj.id))

            for n in range(1, len(my_list)):
                my_list[n] = my_list[n].replace("=", " ")
                attr = shlex.split(my_list[n])
                attr[1] = attr[1].replace("_", " ")

                try:
                    variable = eval(attr[1])
                    attr[1] = variable
                except Exception as e:
                    pass
                if type(attr[1]) is not tuple:
                    setattr(dict_obj, attr[0], attr[1])

            dict_obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, argument):
        """ Shows string representation of the instance passed """

        if not argument:
            print("** class name missing **")
            return

        argv = argument.split(' ')

        if argv[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            for key, value in all_objects.items():
                object_name = value.__class__.__name__
                object_id = str(value.id)
                if object_name == argv[0] and object_id == argv[1]:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, argument):
        """ Removes an instance passed """

        if not argument:
            print("** class name missing **")
            return

        argv = argument.split(' ')

        if argv[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                object_name = value.__class__.__name__
                object_id = str(value.id)
                if object_name == argv[0] and object_id == argv[1]:
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, argument):
        """ Prints all instances of a given class """

        if not argument:
            print("** class name missing **")
            return

        argv = argument.split(' ')

        if argv[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            all_objects = storage.all()
            instances = []
            for key, value in all_objects.items():
                object_name = value.__class__.__name__
                if object_name == argv[0]:
                    instances += [value.__str__()]
            print(instances)

    def do_update(self, argument):
        """ Updates an instance using class name and id """

        if not argument:
            print("** class name missing **")
            return

        a = ""
        for i in argument.split(','):
            a = a + i
        argv = a.split(" ")

        if argv[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            for key, objc in all_objects.items():
                object_name = objc.__class__.__name__
                object_id = str(objc.id)
                if object_name == argv[0] and object_id == argv[1]:
                    if len(argv) == 2:
                        print("** attribute name missing **")
                    elif len(argv) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, argv[2], argv[3])
                        storage.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
