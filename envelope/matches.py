from abc import ABC, abstractmethod, ABCMeta
from typing import List
from envelope.envelopes import EnvelopeOne, EnvelopeTwo
from logger.log import logger

_log = logger()


class Match(ABC):
    """Match object provides 1 method to implement in its subclasses: perform()."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def perform(self) -> int:
        pass


class EnvelopeMatch(Match):
    """Check if envelope one fits into envelope two."""

    def __init__(self, env_one: List[int], env_two: List[int]) -> None:
        self._env_one = EnvelopeOne(env_one[0], env_one[1])
        self._env_two = EnvelopeTwo(env_two[0], env_two[1])

    def perform(self) -> None:
        name_one = self._env_one.__class__.__name__
        name_two = self._env_two.__class__.__name__
        if self._env_one.size() > self._env_two.size():
            _log.info('{e1} does not fit into {e2}, please try again! Reason - {r1} and {r2}'.format(
                e1=name_one,
                e2=name_two,
                r1=self._env_one,
                r2=self._env_two)
            )
            return
        _log.info('Congratulations {e1} fits into {e2}!'.format(e1=name_one, e2=name_two))
        return
