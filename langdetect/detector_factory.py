import os
from os import path
import sys

try:
    import simplejson as json
except ImportError:
    import json

from .detector import Detector
from .profiles import profiles
from .lang_detect_exception import ErrorCode, LangDetectException
from .utils.lang_profile import LangProfile


class DetectorFactory(object):
    '''
    Language Detector Factory Class.

    This class manages an initialization and constructions of Detector.

    Before using language detection library,
    load profiles with DetectorFactory.load_profile(str)
    and set initialization parameters.

    When the language detection,
    construct Detector instance via DetectorFactory.create().
    See also Detector's sample code.
    '''
    seed = None

    def __init__(self):
        self.word_lang_prob_map = {}
        self.langlist = []

    def load_profile(self):
        langsize, index = len(profiles), 0
        for _p in profiles:
            profile = LangProfile(**_p)
            self.add_profile(profile, index, langsize)
            index += 1

    def load_json_profile(self, json_profiles):
        langsize, index = len(json_profiles), 0
        if langsize < 2:
            raise LangDetectException(ErrorCode.NeedLoadProfileError, 'Need more than 2 profiles.')

        for json_profile in json_profiles:
            try:
                json_data = json.loads(json_profile)
                profile = LangProfile(**json_data)
                self.add_profile(profile, index, langsize)
                index += 1
            except:
                raise LangDetectException(ErrorCode.FormatError, 'Profile format error.')

    def add_profile(self, profile, index, langsize):
        lang = profile.name
        if lang in self.langlist:
            raise LangDetectException(ErrorCode.DuplicateLangError, 'Duplicate the same language profile.')
        self.langlist.append(lang)

        for word in profile.freq:
            if word not in self.word_lang_prob_map:
                self.word_lang_prob_map[word] = [0.0] * langsize
            length = len(word)
            if 1 <= length <= 3:
                prob = 1.0 * profile.freq.get(word) / profile.n_words[length - 1]
                self.word_lang_prob_map[word][index] = prob

    def clear(self):
        self.langlist = []
        self.word_lang_prob_map = {}

    def create(self, alpha=None):
        '''Construct Detector instance with smoothing parameter.'''
        detector = self._create_detector()
        if alpha is not None:
            detector.set_alpha(alpha)
        return detector

    def _create_detector(self):
        if not self.langlist:
            raise LangDetectException(ErrorCode.NeedLoadProfileError, 'Need to load profiles.')
        return Detector(self)

    def set_seed(self, seed):
        self.seed = seed

    def get_lang_list(self):
        return list(self.langlist)


_factory = None

def init_factory():
    global _factory
    if _factory is None:
        _factory = DetectorFactory()
        _factory.load_profile(PROFILES_DIRECTORY)

def detect(text):
    init_factory()
    detector = _factory.create()
    detector.append(text)
    return detector.detect()


def detect_langs(text):
    init_factory()
    detector = _factory.create()
    detector.append(text)
    return detector.get_probabilities()
