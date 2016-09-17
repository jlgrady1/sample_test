import time
from tests.base import BaseTest


class TestDelay(BaseTest):
    def test_delay(self):
        time.sleep(10)
        assert 1 == 1
