#!/usr/bin/python3
"""Defining rectangle class"""
from models.base import Base

class Rectangle(Base):
	""" Defining rectangle by inheriting from Base class"""

	def __init__(self, width, height, x=0, y=0, id=None):
		super().__init__(id)
		"""Creating new rectangle.
		Arguments:
		width : width of rectangle
		height : height of rectangle
		x : x co-ord. of rectangle
		y : y co-ord. of rectangle
		id : identity of rectangle
		"""
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	"""Getter and Setters"""
	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, value):
		self.__width = value
		
	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, value):
		self.__height = value

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		 self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value):
		self.__y = value
