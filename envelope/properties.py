from abc import ABC, abstractmethod, ABCMeta


class EnvProperty(ABC):
    """Represents envelope property interface"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def value(self) -> int:
        pass


class PropertyError(Exception):
    """Checks for invalid envelope property value"""

    pass


class SafeProperty(EnvProperty):
    """Concrete safe envelope value"""

    def __init__(self, prop: EnvProperty, wrong_property: int = 0) -> None:
        self._property = prop
        self._error = wrong_property

    def value(self) -> int:
        if not self._property.value() <= self._error:
            return self._property.value()
        raise PropertyError("{} equals to {}. Please specify correct value (has to be more than {})".format(
            self._property.__class__.__name__, self._property.value(), self._error))


class EnvelopeWidth(EnvProperty):
    """Concrete envelope width"""

    def __init__(self, inp: int) -> None:
        self._i = inp

    def value(self) -> int:
        return self._i


class EnvelopeHeight(EnvProperty):
    """Concrete envelope height"""

    def __init__(self, inp: int) -> None:
        self._i = inp

    def value(self) -> int:
        return self._i
