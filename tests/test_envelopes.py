from envelope.envelopes import EnvelopeOne, EnvelopeTwo

_height = 4
_width = 3


def test_envelope_one():
    assert EnvelopeOne(_height, _width).size() == _height * _width


def test_envelope_two():
    assert EnvelopeTwo(_height, _width).size() == _height * _width
