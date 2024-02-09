#!/usr/bin/python3
"""
State Module
Defines the State class, a subclass of BaseModel
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    State Class
    Inherits from BaseModel

    Public class attributes:
        name (str): The name of the state.
    """
    name = ""
