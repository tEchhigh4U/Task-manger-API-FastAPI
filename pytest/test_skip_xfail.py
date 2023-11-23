import pytest
import sys

@pytest.mark.xfail
def test_example():
    assert 1 == 2

@pytest.mark.skip
def test_example_skip():
    assert 1 == 2

# use skip and xfail with conditions and reasons
@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
def test_version_skip():
    assert sys.version_info >= (3, 6)

# The run=True parameter for xfail means the test will be run even if it's expected to fail.
# If run=False, the test would not be run, similar to a skipped test.
@pytest.mark.xfail(sys.version_info < (3, 6), reason="requires python3.6 or higher", run=True)
def test_version_xfail():
    assert sys.version_info >= (3, 6)