import unittest

from langdetect.language import Language


class LanguageTest(unittest.TestCase):
    def test_language(self):
        lang = Language(None, 0)
        self.assertIsNone(lang.lang)
        self.assertEqual(lang.prob, 0.0, 0.0001)
        self.assertEqual(str(lang), '')

        lang2 = Language('en', 1.0)
        self.assertEqual(lang2.lang, 'en')
        self.assertEqual(lang2.prob, 1.0, 0.0001)
        self.assertEqual(str(lang2), 'en:1.0')

    def test_cmp(self):
        lang1 = Language('a', 0.5)
        lang2 = Language('b', 0.1)

        self.assertEqual(cmp(lang1, lang2), -1)
        self.assertEqual(cmp(lang2, lang1), 1)
        self.assertEqual(cmp(lang1, lang1), 0)
