import unittest
from custom_functions import temperature_methods

class Test_temperature_methods(unittest.TestCase):
    def test_high_temperature(self):

        list = [1,2,3,4,5,6,7,8,9]
        max = temperature_methods.high_temperature(list)

        self.assertEqual (max,9))