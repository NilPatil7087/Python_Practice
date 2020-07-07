import unittest
from city_functions import city
from city_functions import city2


class CityTestCases(unittest.TestCase):

    def test_city_country(self):
        info = city("santiago", "chile")
        self.assertEqual(info, "Santiago,Chile")

    def test_city_country_population(self):
        info2 = city2("santiago","chile",5000000)
        self.assertEqual(info2,"Santiago,Chile,Population:5000000")

if __name__ == '__main__':
    unittest.main()
