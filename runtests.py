import sys
import os
import pytest

test_files = ['tests/unit', 'tests/integration']

if len(sys.argv) > 1:
    test_files = sys.argv[1:]

os.environ['PYTHONPATH'] = '.'
status = pytest.main(test_files)
exit(status)
