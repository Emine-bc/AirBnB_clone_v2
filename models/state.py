#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
import models
from sqlalchemy.orm import relationship
import os
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete", backref="state")

    @property
    def cities(self):
        """Return all cities"""
        allc = models.storage.all(City)
        list = []
        for key, value in allc.items():
            if value.state_id == self.id:
                list.append(value)
        return list
