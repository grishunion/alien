
import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
    """Тесты для city_functions"""
    def test_country_city_naming(self):
        formatted_naming = get_formatted_city('moscow', 'russia')
        self.assertEqual(formatted_naming, 'Moscow, Russia.') #Важно все знаки припенания так же указывать в желаемый результат

    def test_country_city_population_naming(self):
        formatted_naming = get_formatted_city('moscow', 'russia', 5000000) 
        self.assertEqual(formatted_naming, 'Moscow, Russia - Population 5000000.')   

if __name__ == '__main__':
    unittest.main()         