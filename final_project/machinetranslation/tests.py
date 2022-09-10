import unittest
import translator

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        # equal
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        # not equal
        self.assertNotEqual(translator.english_to_french('Hello'), 'Hello')
        # null input
        self.assertEqual(translator.english_to_french(None), 'text must be provided')
    
    def test_frenchToEnglish(self):
        # equal
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        # not equal
        self.assertNotEqual(translator.french_to_english('Bonjour'), 'Bonjour')
        # null input
        self.assertEqual(translator.french_to_english(None), 'text must be provided')

if __name__ == '__main__':
    unittest.main()