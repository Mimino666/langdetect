class Language(object):
    '''
    Language is to store the detected language.
    Detector.get_probabilities() returns a list of Languages.
    '''

    def __init__(self, lang, prob):
        self.lang = lang
        self.prob = prob

    def __repr__(self):
        if self.lang is None:
            return ''
        return '%s:%s' % (self.lang, self.prob)

    def __cmp__(self, other):
        if self.prob != other.prob:
            return -1 if self.prob > other.prob else 1
        return 0
