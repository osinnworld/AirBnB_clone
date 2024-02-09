#!/usr/bin/python3
"""
Command-line interpreter for HBNB project.
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class defines the command-line interpreter.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit.
        """
        return True

    def help_quit(self):
        """
        Print help message for quit command.
        """
        print("Quit command to exit.")

    def do_EOF(self, arg):
        """
        Handle EOF (Ctrl+D) to exit.
        """
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()

