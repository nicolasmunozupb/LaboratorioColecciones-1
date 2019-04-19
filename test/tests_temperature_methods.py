import unittest
from custom_functions import temperature_methods


class Test_collection_methods(unittest.TestCase):

    def test_prom_temperature(self):

        list = [28,29,27,33,35,29,34,32,31,34,26,25]
        prom = temperature_methods.prom_temperature(list)

        self.assertEqual(prom,30.25)

    def test_high_temperature(self):

        list = [30,25,26,28,33,35,39,24,25,29,38,25]
        month = temperature_methods.high_temperature(list)

        self.assertEqual(month, ["noviembre"])
    def test_hot_prom(self):

       list = [24,36,38,34,35,29,28,27,26,24,39,40]
       hot = temperature_methods.hot_prom(list)

       self.assertEqual(hot,40)

    def test_standard_deviation(self):

        list = [6,2,3,1]
        result = temperature_methods.standard_deviation(list)

        self.assertEqual(result,1.87)

if __name__ == '__main__':
    unittest.main()




















