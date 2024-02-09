#!/usr/bin/python3
"""
AirBnB Clone - Storage Module
This script initializes the FileStorage engine and reloads the data from the JSON file.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

