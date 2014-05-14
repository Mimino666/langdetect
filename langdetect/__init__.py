from os import path

PROFILES_DIRECTORY = path.join(path.dirname(__file__), 'profiles')
_factory = None


def init_factory():
    from .detector_factory import DetectorFactory
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
