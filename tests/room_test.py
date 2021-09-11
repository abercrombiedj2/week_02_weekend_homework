import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(2)
        self.song = Song("PSY", "Gangnam Style")
        self.guest_1 = Guest("Stan", 25, "Gangnam Style")
        self.guest_2 = Guest("Steve", 25, "Lady In Red")
        self.guest_3 = Guest("Craig", 25, "Billie Jean")
    
    def test_room_has_capacity(self):
        self.assertEqual(2, self.room.capacity)
    
    def test_guest_checked_in(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(1, len(self.room.guests))
    
    def test_guest_checked_out(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_out_guest(self.guest_1)
        self.assertEqual(0, len(self.room.guests))
    
    def test_song_added(self):
        self.room.add_song(self.song)
        self.assertEqual(self.song, self.room.songs[0])
    
    def test_room_reached_capacity(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.room.check_in_guest(self.guest_3)
        self.assertEqual(2, len(self.room.guests))
    
    def test_playlist_has_guest_favourtie_song(self):
        self.room.add_song(self.song.title)
        self.assertEqual("Whoop whoop!", self.room.check_playlist(self.guest_1.favourite_song))