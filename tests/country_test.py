import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    
    def setUp(self):
        self.country = Country("Australia", "Oceania")