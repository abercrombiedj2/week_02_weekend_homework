import unittest

from src.guest import Guest
from src.venue import Venue

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Stan", 25, "Gangnam Style")
        self.venue = Venue("CodeClan Karaoke", 100, 10)
    
    def test_guest_has_name(self):
        self.assertEqual("Stan", self.guest.name)
    
    def test_guest_has_cash(self):
        self.assertEqual(25, self.guest.cash)
    
    def test_guest_cash_decresed(self):
        self.guest.pay_entry_fee(self.venue.entry_fee)
        self.assertEqual(15, self.guest.cash)
