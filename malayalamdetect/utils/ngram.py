import re

import six

from . import messages
from .unicode_block import (
    unicode_block
)


class NGram(object):
    N_GRAM = 3

    def __init__(self):
        self.grams = ' '

    def add_char(self, ch):
        '''Append a character into ngram buffer.'''
        ch = self.normalize(ch)
        last_char = self.grams[-1]
        if last_char == ' ':
            self.grams = ' '
            if ch == ' ':
                return
        elif len(self.grams) >= self.N_GRAM:
            self.grams = self.grams[1:]
        self.grams += ch

    def get(self, n):
        '''Get n-gram.'''
        if n < 1 or n > self.N_GRAM or len(self.grams) < n:
            return
        if n == 1:
            ch = self.grams[-1]
            if ch == ' ':
                return
            return ch
        else:
            return self.grams[-n:]

    @classmethod
    def normalize(cls, ch):
        block = unicode_block(ch)
        return ch
