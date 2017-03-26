import unittest
import pytest

class TestTest(unittest.TestCase):
    """Verify that I could be testing if I wanted to.""" 

    def setUp(self):
        pass

    def test_testing(self):
    	# intentionally failing to check setup
        self.assertTrue(True)
