import unittest

import six

from langdetect.utils import unicode_block


class UnicodeBlockTest(unittest.TestCase):
    def test_unicode_block(self):
        self.assertEqual(unicode_block.unicode_block(six.u('\u0065')), unicode_block.UNICODE_BASIC_LATIN)
        self.assertEqual(unicode_block.unicode_block(six.u('\u007F')), unicode_block.UNICODE_BASIC_LATIN)
        self.assertEqual(unicode_block.unicode_block(six.u('\u0080')), unicode_block.UNICODE_LATIN_1_SUPPLEMENT)
        self.assertEqual(unicode_block.unicode_block(six.u('\u21FF')), unicode_block.UNICODE_ARROWS)
        self.assertEqual(unicode_block.unicode_block(six.u('\u2200')), unicode_block.UNICODE_MATHEMATICAL_OPERATORS)
        self.assertEqual(unicode_block.unicode_block(six.u('\u2201')), unicode_block.UNICODE_MATHEMATICAL_OPERATORS)
        self.assertEqual(unicode_block.unicode_block(six.u('\u22FF')), unicode_block.UNICODE_MATHEMATICAL_OPERATORS)
        self.assertEqual(unicode_block.unicode_block(six.u('\u2300')), unicode_block.UNICODE_MISCELLANEOUS_TECHNICAL)
        # test only on wide builds (i.e. Python 3)
        if len(six.u('\U0010FFFF')) == 1:
            self.assertEqual(unicode_block.unicode_block(six.u('\U000F0000')), unicode_block.UNICODE_SUPPLEMENTARY_PRIVATE_USE_AREA_A)
            self.assertEqual(unicode_block.unicode_block(six.u('\U000FFFFF')), unicode_block.UNICODE_SUPPLEMENTARY_PRIVATE_USE_AREA_A)
            self.assertEqual(unicode_block.unicode_block(six.u('\U00100000')), unicode_block.UNICODE_SUPPLEMENTARY_PRIVATE_USE_AREA_B)
            self.assertEqual(unicode_block.unicode_block(six.u('\U0010FFFF')), unicode_block.UNICODE_SUPPLEMENTARY_PRIVATE_USE_AREA_B)
