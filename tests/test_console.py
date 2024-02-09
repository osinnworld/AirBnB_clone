#!/usr/bin/python3
"""
Module that contains unittest for the console
"""

import os
import console
import pep8
import unittest
from io import StringIO
from unittest.mock import patch
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand

HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    def tearDown(self):
        """Remove file (file.json) created as a result"""
        FileStorage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_help_help(self):
        """tests for help command and text is correct"""
        expected_lines = [
            "Documented commands (type help <topic>):",
            "========================================",
            "Amenity    City  Place   State  all    create   help  show",
            "BaseModel  EOF   Review  User   count  destroy  quit  update"
        ]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            for line in expected_lines:
                self.assertIn(line, output)

    def test_prompt(self):
        """Tests correct format of prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_count(self):
        """Test for the method count"""
        commands = [
            "BaseModel",
            "User",
            "State",
            "Place",
            "City",
            "Amenity",
            "Review"
        ]
        expected_output = "1"
        for cmd in commands:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {cmd}"))
                self.assertFalse(HBNBCommand().onecmd(f"{cmd}.count()"))
                self.assertEqual(expected_output, f.getvalue().strip())

    def test_emptyline(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """Test create with space"""
        with patch('sys.stdout', new=StringIO()) as f:
            commands = [
                "BaseModel",
                "User",
                "State",
                "Place",
                "City",
                "Amenity",
                "Review"
            ]
            for cmd in commands:
                HBNBCommand().onecmd(f"create {cmd}")

    def test_create_notation(self):
        """Test create with dot notation"""
        with patch('sys.stdout', new=StringIO()) as f:
            commands = [
                "BaseModel",
                "User",
                "State",
                "Place",
                "City",
                "Amenity",
                "Review"
            ]
            for cmd in commands:
                HBNBCommand().onecmd(f"{cmd}.create()")

    def test_show(self):
        """Test show with space"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj_test = storage.all()["BaseModel.{}".format(test_value)]
            command = "show BaseModel {}".format(test_value)
            HBNBCommand().onecmd(command)
            self.assertEqual(obj_test.__str__(), f.getvalue().strip())
        msg = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(msg, f.getvalue().strip())

    def test_show_notation(self):
        """Test show with dot notation"""
        msg = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
            self.assertEqual(msg, f.getvalue().strip())
        msg = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(6767)")
            self.assertEqual(msg, f.getvalue().strip())
        msg = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(msg, f.getvalue().strip())

    def test_all(self):
        """Test all with space"""
        with patch("sys.stdout", new=StringIO()) as f:
            commands = [
                "BaseModel",
                "User",
                "State",
                "Place",
                "City",
                "Amenity",
                "Review"
            ]
            for cmd in commands:
                self.assertFalse(HBNBCommand().onecmd(f"create {cmd}"))
            self.assertFalse(HBNBCommand().onecmd("all"))
            for cmd in commands:
                self.assertIn(cmd, f.getvalue().strip())
        msg = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all latitude"))
            self.assertEqual(msg, f.getvalue().strip())

    def test_all_notation(self):
        """Test all with dot notation"""
        with patch("sys.stdout", new=StringIO()) as f:
            commands = [
                "BaseModel",
                "User",
                "State",
                "City"
            ]
            for cmd in commands:
                self.assertFalse(HBNBCommand().onecmd(f"create {cmd}"))
            for cmd in commands:
                self.assertFalse(HBNBCommand().onecmd(f"{cmd}.all()"))
                self.assertIn(cmd, f.getvalue().strip())

if __name__ == "__main__":
    unittest.main()

