import unittest
from translator import english_to_french, french_to_english

class Test_englishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test2(self): 
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
    
class Test_frenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test2(self): 
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()