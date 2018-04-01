from envelope.properties import EnvelopeWidth, EnvelopeHeight

_width = 3
_height = 4


def test_envelope_width():
    assert EnvelopeWidth(_width).value() == 3


def test_envelope_height():
    assert EnvelopeHeight(_height).value() == 4
