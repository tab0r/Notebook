from math import sqrt


class Point(object):
    '''
    A 2d point class
    '''
    def __init__(self, x, y):
        '''
        Initialize a point with the given x and y coordinate values.
        '''
        self.x = x
        self.y = y

    def __repr__(self):
        '''
        Return a string representation of the point.
        '''
        pass

    def __eq__(self, other):
        '''
        INPUT:
            - other: Point
        Return True iff this is the same point as other.
        '''
        pass

    def __add__(self, other):
        '''
        INPUT:
            - other: Point
        Return a new Point which adds the x and y coordinates of the two points
        together.
        '''
        pass

    def __sub__(self, other):
        '''
        INPUT:
            - other: Point
        Return a new Point which subtracts the x and y coordinates of the second
        point from the first.
        '''
        pass

    def __mul__(self, factor):
        '''
        INPUT:
            - factor: int/float
        Return a new Point which multiplies both the x and y coordinate values
        by the given value.
        '''
        pass

    def length(self):
        '''
        Return the length of the vector (squareroot of the sum of the squares of the components)
        '''
        pass

    def dist(self, other):
        '''
        Return the distance (float) between this point and the other point given.

        Hint: You should use subtract and length!
        '''
        pass


class Triangle(object):
    pass
