#!/usr/bin/python3
"""Contains the Amenity model"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity

class Amenity(BaseModel):
    """Implements the Amenity model"""
  __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
