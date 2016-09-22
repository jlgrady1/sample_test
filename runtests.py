import sys
import os
import pytest

test_files = ['tests/unit', 'tests/integration']

if len(sys.argv) > 1:
    test_files = sys.argv[1:]

os.environ['PYTHONPATH'] = '.'

opts = [
    '-svvvv',
    '--junitxml=/tmp/test.xml',
]

test_files_str = " ".join(test_files)
opts_str = " ".join(opts)
status = pytest.main('{} {}'.format(test_files_str, opts_str))
exit(status)
