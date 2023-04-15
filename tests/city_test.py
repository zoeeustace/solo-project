import unittest
from models.city import City

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.city = City("Sydney", "Australia", True)
    
    
    def test_city_has_name(self):
        self.assertEqual("Sydney", self.city.name)
        
        
    def test_city_has_country_attached(self):
        self.assertEqual("Australia", self.city.country)
       
    
    def test_city_visited_true(self):
        self.assertEqual(True, self.city.visited)
        
    
    # def test_can_mark_test_complete(self):
    #     self.task.mark_complete()
    #     self.assertEqual(True, self.task.completed)