import pytest
from pythonisms import MyCollection

"""
Testing:
For all of the features described, we can create unit tests using the unittest module in python. Here is an example of how to test the __iter__ method of the MyCollection class:
"""


class TestMyCollection:
    # @pytest.fixture
    def collection(self):
        return MyCollection()

    def test_iter(self, collection):
        result = [i for i in collection]
        assert result == [1, 2, 3, 4, 5]
