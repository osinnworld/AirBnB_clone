#!/usr/bin/python3

import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorageInstantiation(unittest.TestCase):
    """
    Test cases for FileStorage instantiation.
    """

    def test_FileStorage_instantiation_no_args(self):
        # Test creating a FileStorage instance with no arguments.
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        # Test creating a FileStorage instance with an argument
        # should raise TypeError.
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        # Test if the storage variable in models is an instance of FileStorage.
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage class methods.
    """

    def setUp(self):
        # Create a temporary test file for saving data.
        self.test_file = "test_file.json"

    def tearDown(self):
        # Remove the temporary test file after the test.
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_returns_dictionary(self):
        # Test if the all() method returns a dictionary.
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new(self):
        # Test the new method by creating and storing a new object.
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new_with_args(self):
        # Test creating a new object with additional arguments
        # should raise TypeError.
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        # Test creating a new object with None (should raise AttributeError).
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        # Test saving objects to a file and then reloading them.
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        # Create a new storage instance to simulate reloading.
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the reloaded objects match the original objects.
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None)

    def test_save_to_file(self):
        # Test saving objects to a file and check if the file is created.
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empty_file(self):
        # Test reloading when the file is empty or does not exist
        # Should not raise any exceptions.
        models.storage.reload()

if __name__ == '__main__':
    unittest.main()

