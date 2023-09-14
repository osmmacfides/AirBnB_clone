#!/usr/bin/python3
"""
This module defines a program that contains
the entry point of the command interpreter:
"""
import cmd
from models.base_model import BaseModel


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

    def do_create(self, line):
	"""
	method to create new instance of BaseModel
	"""
	args = line.split()
	if not args:
		print("** class name missing **")
	else:
		class_name = args[0]
		if class_name != "BaseModel":
			print("** class doesn't exist **")
		else:
			new_instance = BaseModel
			new_instance.save()
			print(new_instance.id)

    def do_show(self):
	"""
	method to print the string representation of an
	instance based on the class name and id
	"""
	args = line.split()
	if not args:
		print("** class name missing **")
		return

	class_name = args[0]
	if class_name != "BaseModel":
		print("** class doesn't exist **")
		return

	if len(args) < 2:
		print("** instance id missing **")
		return

	instance_id = args[1]
	# Attempt to retrieve the instance based on class_name and instance_id
	try:
		instance = storage.get(class_name, instance_id)
		if instance:
			print(instance)
		else:
			print("** no instance found **")
	except Exception as e:
		pass

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
    	if class_name != "BaseModel":
        	print("** class doesn't exist **")
        	return

    	if len(args) < 2:
        	print("** instance id missing **")
        	return

    	instance_id = args[1]
    	try:
        	# Attempt to retrieve the instance based on class_name and instance_id
        	instance = storage.get(class_name, instance_id)
        	if instance:
            	storage.delete(instance)
            	storage.save()
        	else:
           	print("** no instance found **")
    	except Exception as e:
        	pass

    def do_all(self):
	"""
	method to prints all string representation of all
	instances based or not on the class name
	"""
	args = line.split()
	if class_name != "BaseModel":
                print("** class doesn't exist **")
                return

	class_name = args[0]

	if class_name not in ["BaseModel", "User", "State", "City", "Place", "Review", "Amenity"]:
		print ("** class doesn't exist **")
        	return

	instances = storage.all(class_name)
	print([str(instance) for instance in instances])

    def do_update(self):
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
	if class_name != "BaseModel":
		print("** class doesn't exist **")
                return

	if len(args) < 2:
		print("** instance id missing **")
		return

	instance_id = args[1]

	instance = storage.get(class_name. instance_id)
	if not instance:
		print ("** no instance found **")
		return

	if len(args < 4):
		print ("** attribute name missing **")
		return

	attribute_name = args[2]
	attribute_value = " ".join[args[3:]

	if hasattr(instance, attribute_name):
		setattr(instance, attribute_name,
			type(getattr(instance, attribute_name))(attribute_value))
	else:
		print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
