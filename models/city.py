#!/usr/bin/python3
"""
City Module
Defines the City class, a subclass of BaseModel
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City Class
    Inherits from BaseModel

    Attributes:
        state_id (str): The ID of the state associated with the city.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
