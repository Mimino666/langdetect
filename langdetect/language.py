class Language:
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
        return '{}:{}'.format(self.lang, self.prob)

    def __lt__(self, other):
        return self.prob < other.prob
