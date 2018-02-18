"""
Name : Amelie Cameron
Due Date : 12/16/17

Description : Assignment 5 Python OOP

"""
import math
import Point

class Circle(Point.Point):
   
    def __init__(self, x=0, y=0, radius=0):
        super(Circle, self).__init__(x, y)
        self._radius = radius

    def get_radius(self):
        return self._radius

    def __eq__(self, other):
        same_rad = self.get_radius() == other.get_radius()
        same_x = self.get_x() == other.get_x()
        same_y = self.get_y() == other.get_y()
        
        return same_rad and same_x and same_y

    def __repr__(self):
        return '(x = %s, y = %s, r = %s)' % (self._x, self._y, self._radius)

    def __str__(self):
        return '(x = %s, y = %s, r = %s)' % (self._x, self._y, self._radius)

    def area(self):
        return math.pi*self._radius**2

    def circumference(self):
        return math.pi*self._radius*2

    def edge_dist_from_origin(self):
        return self.dist_from_origin() - self._radius

    def circle_intersect_with(self, circle):
        return (self.dist_from_point(circle) - (self.get_radius() + circle.get_radius())) < 0

if __name__ == '__main__':
    c = Circle(3, 4, 1)
    c2 = Circle(4, 5, 1)
    c3 = Circle(3, 4, 1)
    
    print("Circle 1: %s" % repr(c))
    print("Circle 1 Area: %f" % c.area())
    print("Circle 1 Circumference: %f" % c.circumference())
    print("Edge Distance From Origin: %f" % c.edge_dist_from_origin())
    print("Circle 2: %s" % repr(c2))
    print("Instersection with Circle 2 (y=1, n=0): %d" % c.circle_intersect_with(c2))


    assert c.get_radius() == 1
    assert (c.area() - 3.14) < 0.01
    assert (c.circumference() - 6.2831) < 0.01
    assert c.edge_dist_from_origin() == 4.0
    
