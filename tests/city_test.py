import unittest
from models.city import City

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.city = City("Sydney", "Australia", True)
    
    
    # def test_album_has_title(self):
    #     self.assertEqual("Wonderland", self.album.title)
        
        
    # def test_album_has_genre(self):
    #     self.assertEqual("pop", self.album.genre)
       
        
    # def test_album_has_artist(self):
    #     self.assertEqual("McFly", self.album.artist)
    
    
    # def test_task_completed_starts_false(self):
    #     self.assertEqual(False, self.task.completed)
        
    
    # def test_can_mark_test_complete(self):
    #     self.task.mark_complete()
    #     self.assertEqual(True, self.task.completed)