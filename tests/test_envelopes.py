from envelope.envelopes import BirthdayEnvelope, ChristmasEnvelope

_height = 4
_width = 3


def test_birthday_envelope():
    assert BirthdayEnvelope(_height, _width).size() == _height * _width


def test_christmas_envelope():
    assert ChristmasEnvelope(_height, _width).size() == _height * _width
