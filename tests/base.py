import logging
import sys

from datetime import datetime

log = logging.getLogger('base')
log.setLevel('INFO')


class BaseTest(object):
    _TEST_START = None

    @classmethod
    def setup_class(cls):
        cls._TEST_START = datetime.utcnow()

    @classmethod
    def teardown_class(cls):
        now = datetime.utcnow()
        duration = now - cls._TEST_START
        sys.stdout.write("{} duration: {}s".format(cls.__name__, duration.seconds))
