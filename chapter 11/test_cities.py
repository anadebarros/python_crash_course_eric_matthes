import unittest
import city_functions


class TestsCityFunctions(unittest.TestCase):

    def test_city_country(self):
        self.assertEqual(city_functions.city_country(
            "santiago", "chile"), "santiago, chile, ")

    def test_city_country_population(self):
        self.assertEqual(city_functions.city_country(
            "santiago", "chile", population=40000), "santiago, chile, 40000")


if __name__ == "__main__":
    unittest.main()
