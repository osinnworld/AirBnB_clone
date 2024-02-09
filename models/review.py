#!/usr/bin/python3
"""
Review Module
Defines the Review class, a subclass of BaseModel
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review Class
    Inherits from BaseModel

    Public class attributes:
        place_id (str): The ID of the place associated with the review (will be Place.id).
        user_id (str): The ID of the user who wrote the review (will be User.id).
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
