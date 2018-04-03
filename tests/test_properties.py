import pytest
from envelope.properties import EnvelopeWidth, EnvelopeHeight, SafeProperty, PropertyError

_width = 3
_height = 4


def test_envelope_width():
    assert EnvelopeWidth(_width).value() == 3


def test_envelope_height():
    assert EnvelopeHeight(_height).value() == 4


def test_safe_width():
    with pytest.raises(PropertyError):
        SafeProperty(EnvelopeWidth(0)).value()


def test_safe_height():
    with pytest.raises(PropertyError):
        SafeProperty(EnvelopeHeight(0)).value()
