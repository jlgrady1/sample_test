import time

from tests.base import BaseTest


class TestMock(BaseTest):
    def test_1(self):
        time.sleep(5)

    def test_2(self):
        time.sleep(3)
