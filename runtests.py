import sys
import os
import pytest

test_files = 'tests/unit tests/integration'

if len(sys.argv) > 1:
    test_files = ' '.join(sys.argv[1:])
    init = False

os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))

status = pytest.main('{}'.format(test_files))
exit(status)
