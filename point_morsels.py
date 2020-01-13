class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, anotherpoint):
        return self.x == anotherpoint.x and self.y == anotherpoint.y and self.z == anotherpoint.z
        
    def __add__(self, anotherpoint):
        new_x = self.x + anotherpoint.x
        new_y = self.y + anotherpoint.y
        new_z = self.z + anotherpoint.z
        return Point(new_x, new_y, new_z)

    def __sub__(self, anotherpoint):
        new_x = self.x - anotherpoint.x
        new_y = self.y - anotherpoint.y
        new_z = self.z - anotherpoint.z
        return Point(new_x, new_y, new_z)

    def __mul__(self, scalar):
        new_x = self.x * scalar
        new_y = self.y * scalar
        new_z = self.z * scalar
        return Point(new_x, new_y, new_z)
    
    def __rmul(self, scalar):
        return self.__mul__(scalar)

    def __iter__(self):
        #in order to facilitate tuple unpacking we need to make our point iterable
        yield self.x
        yield self.y
        yield self.z
        

    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"


p1 = Point(1,2,3)
p2 = Point(1,2,3)
p1
p2
assert (p1 == p2) == True
