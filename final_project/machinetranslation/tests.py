"""
Tests functions defined in translator.py
"""

import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Class to test translations from English to French
    """
    def test_english_to_french(self):
        """
        Tests translations from English to French
        """
        self.assertEqual(english_to_french(None),None)
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    """
    Class to test translations from French to English
    """
    def test_french_to_english(self):
        """
        Tests translations from French to English
        """
        self.assertEqual(french_to_english(None),None)
        self.assertEqual(french_to_english('Bonjour'),'Hello')

if __name__ == "__main__":
    unittest.main()
