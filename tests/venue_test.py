import unittest

from src.venue import Venue
from src.room import Room
from src.guest import Guest

class TestVenue(unittest.TestCase):

    def setUp(self):
        self.venue = Venue("CodeClan Karaoke", 100, 10)
        self.room = Room(9)
        self.guest = Guest("Stan", 25, "Gangnam Style")

    def test_venue_has_name(self):
        self.assertEqual("CodeClan Karaoke", self.venue.name)
    
    def test_room_added(self):
        self.venue.add_room(self.room)
        self.assertEqual(1, len(self.venue.rooms))
    
    def test_venue_till_increased(self):
        self.venue.take_entry_fee(self.venue.entry_fee)
        self.assertEqual(110, self.venue.till)
