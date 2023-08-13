#!/usr/bin/python3
"""Defines the States class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a states.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
