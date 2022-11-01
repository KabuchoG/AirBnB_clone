#!/usr/bin/python3
"""
Console - entry point of the command interpreter
"""
import cmd
from posixpath import split
from shlex import shlex
from models import storage
from models import review
from models.base_model import BaseModel
import shlex

from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand"""
    prompt = '(hbnb) '
    cls_list = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                "City": City, "Place": Place, "review": review, "State": State}

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of File"""
        return True

    def do_create(self, line):
        """
        Usage: create <class>
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        split_line = line.split()
        if len(split_line) == 0:
            print("** class name missing **")
            return
        count = 1
        for cls in self.cls_list.keys():
            if cls != split_line[0]:
                count = 0
            else:
                count = 1
                break
        if count == 0:
            print("** class doesn't exist **")
            return
        for k in self.cls_list.keys():
            if k == split_line[0]:
                obj = self.cls_list[k]()
                break
        print("{}".format(obj.id))
        storage.save()

    def emptyline(self):
        """ empty line """
        pass

    def do_show(self, line):
        """
        Usage: show <class> <object id>
        Prints the string representation of an instance based on
        the class name and id.
        """
        l_split = line.split()

        if len(l_split) == 0:
            print("** class name missing **")
            return
        for cls in self.cls_list.keys():
            if cls != l_split[0]:
                count = 0
            else:
                count = 1
                break
        if count == 0:
            print("** class doesn't exist **")
            return
        if len(l_split) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        correct_id = ""
        for k in all_objs.keys():
            if all_objs[k].id == l_split[1]:
                correct_id = l_split[1]
        if correct_id == "":
            print("** no instance found **")
            return

        for cls in self.cls_list.keys():
            if cls == l_split[0]:
                for k in all_objs.keys():
                    if all_objs[k].id == l_split[1]:
                        print(all_objs[k])
                        return

    def do_destroy(self, line):
        """
        Usage: destroy <class> <object id>
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        if line == "":
            print("** class name missing **")
            return
        l_split = line.split()

        for cls in self.cls_list.keys():
            if cls != l_split[0]:
                count = 0
            else:
                count = 1
                break
        if count == 0:
            print("** class doesn't exist **")
            return
        if len(l_split) == 1:
            print("** instance id missing **")
            return
        correct_id = ""
        all_objs = storage.all()
        for k in all_objs.keys():
            if all_objs[k].id == l_split[1]:
                correct_id = l_split[1]
        if correct_id == "":
            print("** no instance found **")
            return

        for cls in self.cls_list.keys():
            if cls == l_split[0]:
                all_objs = storage.all()
                for k in all_objs.keys():
                    if all_objs[k].id == l_split[1]:
                        del all_objs[k]
                        storage.save()
                        return

    def do_all(self, line):
        """
        Usage: All, All <class>
        Prints all string representation of all instances based
        or not on the class name.
        """
        l_split = line.split()
        count = 1
        if line != "":
            for cls in self.cls_list.keys():
                if cls != l_split[0]:
                    count = 0
                else:
                    count = 1
                    break
        if count == 0:
            print("** class doesn't exist **")
            return
        else:
            all_objs = storage.all()
            if len(l_split) == 1:
                for obj_id in all_objs.keys():
                    if all_objs[obj_id].__class__.__name__ == l_split[0]:
                        obj = all_objs[obj_id]
                        print(obj)
                return
            elif len(l_split) == 0:
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    print(obj)
                return

    def do_update(self, line):
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name and id by
        adding or updating attribute
        """
        split_line = shlex.split(line)
        count = 1
        if len(split_line) == 0:
            print("** class name missing **")
            return
        for cls in self.cls_list.keys():
            if cls != split_line[0]:
                count = 0
            else:
                count = 1
                break
        if count == 0:
            print("** class doesn't exist **")
            return
        if len(split_line) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        correct_id = ""
        for k in all_objs.keys():
            if all_objs[k].id == split_line[1]:
                correct_id = split_line[1]
                break
        if correct_id == "":
            print("** no instance found **")
            return
        if len(split_line) == 2:
            print("** attribute name missing **")
            return
        if len(split_line) == 3:
            print("** value missing **")
            return
        setattr(storage.all()[k], split_line[2], split_line[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
