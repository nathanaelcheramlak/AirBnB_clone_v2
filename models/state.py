#!/usr/bin/python3
"""Module for State"""
import models
import shlex
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Class State representation"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Property that connect cities to states"""
        var = models.storage.all()
        list_all = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                list_all.append(var[key])
        for elem in list_all:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
