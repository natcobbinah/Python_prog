from city_functions import city_country
import unittest

class CityCountryTest(unittest.TestCase):

    def test_city_country(self):
        """Pair city with country"""
        merged_name = city_country('Santiago','Chile')
        self.assertEqual(merged_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Pair city with country and population"""
        merged_args = city_country('Santiago','Chile','5000000')
        self.assertEqual(merged_args, 'Santiago, Chile - population 5000000')
    
if __name__ == '__main__':
    unittest.main()