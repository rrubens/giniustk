#from __future__ import unicode_literals, print_function

from unittest import TestCase
from giniustk.utils import utils

class Test(TestCase):
    def test_sum(self):
        assert utils.sum(3, 2) == 5


    def test_hw(self):
        assert utils.HW() == "Hello World"
        assert utils.HW() != "HW"


    def test_greater_than(self):
        assert utils.greaterThan(50) is True
        assert utils.greaterThan(7) is False

    def test_smaller_than(self):
        assert utils.smallerThan(50) is False
        assert utils.smallerThan(7) is True

    def test_is_true(self):
        assert utils.isTrue() is True

    def test_is_False(self):
        assert utils.isTrue() is False
