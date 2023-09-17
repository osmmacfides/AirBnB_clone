#!/usr/bin/python3
"""
This module defines a program that contains
the entry point of the command interpreter:
"""
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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

    def do_help(self, arg):
        """
        List available commands with "help" or detailed help with "help cmd"
        """
        return super().do_help(arg)

    def do_EOF(self, line):
        """
        method to exit the program
        """
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, line):
        """
        method to create new instance of BaseModel
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City",
                              "Place", "Review", "Amenity"]:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        method to print the string representation of an
        instance based on the class name and id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in ["BaseModel", "User", "State", "City",
                              "Place", "Review", "Amenity"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instance = storage.get(class_name, instance_id)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        method to delete an instance based on the class name
        and id (save the change into the JSON file)
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in ["BaseModel", "User", "State", "City",
                              "Place", "Review", "Amenity"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instance = storage.get(class_name, instance_id)
        if instance:
            storage.delete(instance)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        method to prints all string representation of all
        instances based or not on the class name
        """
        args = line.split()

        class_name = args[0]

        if args and class_name not in ["BaseModel", "User", "State", "City",
                              "Place", "Review", "Amenity"]:
            print("** class doesn't exist **")
            return

        instances = storage.all(args[0] if args else None)
        print([str(instance) for instance in instances.values()])

    def do_update(self, line):
        """
        method to Updates an instance based on the class name
        and id by adding or updating attribute (save the
        change into the JSON file)
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City",
                              "Place", "Review", "Amenity"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
	instance = storage.get(class_name, instance_id)
        if not instance:
            print("** no instance found **")
            return

        if len(args) < 4:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if attribute_name == "id" or attribute_name == "created_at" or attribute_name == "updated_at":
            print("** cannot update id, created_at, or updated_at **")
            return

	if len(args) < 5:
            print("** value missing **")
            return

        attribute_value = args[3]

        # Check if the attribute value is enclosed in double quotes and strip them if present
        if attribute_value.startswith('"') and attribute_value.endswith('"'):
            attribute_value = attribute_value[1:-1]

        # Get the current attribute type
        attr_type = type(getattr(instance, attribute_name))

        # Cast the attribute value to the attribute type
        try:
            casted_value = attr_type(attribute_value)
        except ValueError:
            print("** invalid attribute value **")
            return

	# Update the attribute
        setattr(instance, attribute_name, casted_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
