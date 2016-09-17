import cmath


class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    @classmethod
    def get_distance(cls, x1, x2):
        return abs(x1 - x2)

    def distance_to_point(self, point):
        a = self.get_distance(self.x, point.x)
        b = self.get_distance(self.y, point.y)
        distance = cmath.sqrt(a ** 2 + b ** 2)
        return distance
