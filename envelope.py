import argparse
from typing import List
from envelope.envelopes import BirthdayEnvelope, ChristmasEnvelope
from logger.log import logger


_log = logger()


class Match:
    def __init__(self, args_one: List[int], args_two: List[int]) -> None:
        self._bday_env = BirthdayEnvelope(args_one[0], args_one[1])
        self._chr_env = ChristmasEnvelope(args_two[0], args_two[1])

    def run(self) -> None:
        name_one = self._bday_env.__class__.__name__
        name_two = self._chr_env.__class__.__name__
        if self._bday_env.size() > self._chr_env.size():
            return _log.info('{e1} does not fit into {e2}, please try again! Reason {r1} and {r2}'.format(
                e1=name_one,
                e2=name_two,
                r1=self._bday_env,
                r2=self._chr_env)
            )
        return _log.info('Congratulations {e1} fits into {e2}!'.format(e1=name_one, e2=name_two))


if __name__ == '__main__':
    _parser = argparse.ArgumentParser(description="This program allows to check if envelope1 fits into envelope2.")
    _parser.add_argument("--envelope1", "-en1", help="Size for envelope1 (1x2)", nargs=2, type=int, required=True)
    _parser.add_argument("--envelope2", "-en2", help="Size for envelope2 (1x2)", nargs=2, type=int, required=True)
    args = _parser.parse_args()
    Match(args.envelope1, args.envelope2).run()
