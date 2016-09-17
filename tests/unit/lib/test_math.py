import time

from tests.base import BaseTest
from lib.math import Point


class TestPoint(BaseTest):
    def test_something(self):
        time.sleep(10)
        assert 1 == 1

    def test_get_distance(self):
        d1 = Point.get_distance(5, 0)
        d2 = Point.get_distance(3, 10)
        assert d1 == 5
        assert d2 == 7

    def test_distance_to_point(self):
        p1 = Point(0, 0)
        p2 = Point(0, 5)
        assert p1.distance_to_point(p2) == 5
