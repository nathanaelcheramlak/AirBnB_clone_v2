#!/usr/bin/python3
"""Module for State"""
from models.base_model import BaseModel
from sqlalchemy import Column, String

class State(BaseModel):
    """Class State representation"""
    __tabelname__ = "states"
    name = Column(String(128), nullable=False)
