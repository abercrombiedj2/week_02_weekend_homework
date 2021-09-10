import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Stan", 25)
    
    def test_guest_has_name(self):
        self.assertEqual("Stan", self.guest.name)
    
    def test_guest_has_cash(self):
        self.assertEqual(25, self.guest.cash)