import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Chris De Burgh", "Lady In Red")
    
    def test_song_has_title(self):
        self.assertEqual("Lady In Red", self.song.title)
    
    def test_song_has_artist(self):
        self.assertEqual("Chris De Burgh", self.song.artist)