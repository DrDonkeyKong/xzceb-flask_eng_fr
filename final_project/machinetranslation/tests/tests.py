import unittest
from .. import translator

class TestTranslatorString(unittest.TestCase):

    def test_englishToFrench1(self):
        translation = translator.englishToFrench(None)
        self.assertEqual(translation, "")

    def test_englishToFrench2(self):
        translation = translator.englishToFrench("")
        self.assertEqual(translation, "")

    def test_englishToFrench3(self):
        translation = translator.englishToFrench("Hello")
        self.assertEqual(translation, "Bonjour")

    def test_frenchToEnglish1(self):
        translation = translator.englishToFrench(None)
        self.assertEqual(translation, "")

    def test_frenchToEnglish2(self):
        translation = translator.englishToFrench("")
        self.assertEqual(translation, "")

    def test_frenchToEnglish3(self):
        translation = translator.frenchToEnglish("Bonjour")
        self.assertEqual(translation, "Hello")

if __name__ == '__main__':
    unittest.main()