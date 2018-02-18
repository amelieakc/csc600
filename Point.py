"""
Name : Amelie Cameron
Due Date : 12/16/17

Description : Assignment 5 Python OOP

"""

import math

class Point(object):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

    def __eq__(self, other):
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()

    def __repr__(self):
        return '(x = %s, y = %s)' % (self._x, self._y)

    def __str__(self):
         return '(x = %s, y = %s)' % (self._x, self._y)

    def dist_from_origin(self):
        return math.sqrt((self.get_x())**2 + (self.get_y())**2) 

    def dist_from_point(self, point):
        return math.sqrt((self.get_x() - point.get_x())**2 + (self.get_y() - point.get_y())**2) 


if __name__ == '__main__':
    p = Point(3, 4)
    p2 = Point(4, 5)
    p3 = Point(3, 4)

    print("Point 1: %s" % repr(p))
    print("Distance from origin: %f" % p.dist_from_origin())
    print("Point 2: %s" %  repr(p2))
    print("Distance from Point 2: %f" % p.dist_from_point(p2))
    print("Point 3: %s" % repr(p3))
     
    
    assert p.dist_from_origin() == 5.0
    assert (p.dist_from_point(p2) - 1.4142) < 0.01
