from abc import ABC, abstractmethod, ABCMeta
from envelope.properties import SafeProperty, EnvelopeWidth, EnvelopeHeight


class Envelope(ABC):
    """Envelope provides 2 methods to implement in its subclasses: size() and __str__()"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class BirthdayEnvelope(Envelope):
    """Concrete envelope object"""

    def __init__(self, height: int, width: int) -> None:
        self._height = SafeProperty(EnvelopeHeight(height))
        self._width = SafeProperty(EnvelopeWidth(width))

    def size(self) -> int:
        return self._height.value() * self._width.value()

    def __str__(self) -> str:
        return "{} has size {}x{}".format(self.__class__.__name__, self._height.value(), self._width.value())


class ChristmasEnvelope(Envelope):
    """Concrete envelope object"""

    def __init__(self, height: int, width: int) -> None:
        self._height = SafeProperty(EnvelopeHeight(height))
        self._width = SafeProperty(EnvelopeWidth(width))

    def size(self) -> int:
        return self._height.value() * self._width.value()

    def __str__(self) -> str:
        return "{} has size {}x{}".format(self.__class__.__name__, self._height.value(), self._width.value())
