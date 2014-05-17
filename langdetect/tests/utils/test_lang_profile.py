import unittest

import six
from six.moves import xrange

from langdetect.utils.lang_profile import LangProfile


class LangProfileText(unittest.TestCase):
    def test_lang_profile(self):
        profile = LangProfile()
        self.assertTrue(profile.name is None)

    def test_lang_profile_string_int(self):
        profile = LangProfile('en')
        self.assertEqual(profile.name, 'en')

    def test_add(self):
        profile = LangProfile('en')
        profile.add('a')
        self.assertEqual(profile.freq.get('a'), 1)
        profile.add('a')
        self.assertEqual(profile.freq.get('a'), 2)
        profile.omit_less_freq()

    def test_add_illegally1(self):
        profile = LangProfile()
        profile.add('a')  # ignore
        self.assertTrue(profile.freq.get('a') is None)  # ignored

    def test_add_illegally2(self):
        profile = LangProfile('en')
        profile.add('a')
        profile.add('')  # Illegal (string's length of parameter must be between 1 and 3) but ignore
        profile.add('abcd')  # as well
        self.assertEqual(profile.freq.get('a'), 1)
        self.assertTrue(profile.freq.get('') is None)  # ignored
        self.assertTrue(profile.freq.get('abcd') is None)  # ignored

    def test_omit_less_freq(self):
        profile = LangProfile('en')
        grams = six.u('a b c \u3042 \u3044 \u3046 \u3048 \u304a \u304b \u304c \u304d \u304e \u304f').split()
        for i in xrange(5):
            for g in grams:
                profile.add(g)
        profile.add(six.u('\u3050'))

        self.assertEqual(profile.freq.get('a'), 5)
        self.assertEqual(profile.freq.get(six.u('\u3042')), 5)
        self.assertEqual(profile.freq.get(six.u('\u3050')), 1)
        profile.omit_less_freq()
        self.assertTrue(profile.freq.get('a') is None)  # omitted
        self.assertEqual(profile.freq.get(six.u('\u3042')), 5)
        self.assertTrue(profile.freq.get(six.u('\u3050')) is None)  # omitted

    def test_omit_less_freq_illegally(self):
        profile = LangProfile()
        profile.omit_less_freq()  # ignore
