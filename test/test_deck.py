import unittest

from src.deck import Deck

class TestDeckMethods(unittest.TestCase):
    
    def test_createDeck(self):
        d = Deck()
        self.assertIsInstance(d, Deck())

if __name__ == "__main__":
    unittest.main()