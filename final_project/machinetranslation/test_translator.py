import unittest
import translator

class TestTranslator(unittest.TestCase):
    def test_englishToFrench_assertEqual(self):
        # equal
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        # null input
        self.assertEqual(translator.english_to_french(None), 'text must be provided')
    
    def test_englishToFrench_assertNotEqual(self):
        # not equal
        self.assertNotEqual(translator.english_to_french('Hello'), 'Hello')
    
    def test_frenchToEnglish_assertEqual(self):
        # equal
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        # null input
        self.assertEqual(translator.french_to_english(None), 'text must be provided')

    def test_frenchToEnglish_assertNotEqual(self):
        # not equal
        self.assertNotEqual(translator.french_to_english('Bonjour'), 'Bonjour')

if __name__ == '__main__':
    unittest.main(verbosity=2)