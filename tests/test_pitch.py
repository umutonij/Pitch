import unittest
from app.models import Pitch

class PostModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch= Pitch(id = 1, pitch_title = 'Python', pitch_content = 'Programming language that helps to build application')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    

if __name__ == '__main__':
    unittest.main()