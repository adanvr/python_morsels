import math

#Here I am setting all of our attributes in our initializer method, which gets run each time a new instance of our class is created.
#Additionally, we can add a useful string representation using the __repr__ method
#In order for the area and diameter to change automatically when we change the radius we need to make the diameter and area attributes into properties


class Circle:
    def __init__(self, radius = 1):
        self.radius = radius
    
    def __repr__(self):
        return f'Circle({self.radius})'
    #whenever the area and diameter attributes are accessed, the corresponding methods will be executed and the returned value will be 
    # provided as the value of the accessed attribute.
    @property
    def area(self):
        self.area = (self.radius ** 2) * math.pi
    #The second bonus required that the diameter property be able to be set to a value and that the radius would automatically change appropriately based on the set value.
    #For this we need to make a setter for our diameter property.
    @property
    def diameter(self):
        self.diameter = self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius can't be negative")
        self._radius = radius
    