import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(9)
    
    def test_room_has_capacity(self):
        self.assertEqual(9, self.room.capacity)