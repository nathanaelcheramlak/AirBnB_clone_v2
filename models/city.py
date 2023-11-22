#!/usr/bin/python3
"""Module for City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel):
    """Class City representation"""
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("state_id"), nullable=False)
    name = Column(String(128), nullable=False)
