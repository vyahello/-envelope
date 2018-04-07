import argparse
from envelope.matches import EnvelopeMatch

if __name__ == '__main__':
    _parser = argparse.ArgumentParser(description="This program allows to check if envelope1 fits into envelope2.")
    _parser.add_argument("--envelope1", "-en1", help="Size for envelope1 (like `1x2`)", nargs=2, type=int,
                         required=True)
    _parser.add_argument("--envelope2", "-en2", help="Size for envelope2 (like `1x2`)", nargs=2, type=int,
                         required=True)
    args = _parser.parse_args()
    EnvelopeMatch(args.envelope1, args.envelope2).perform()
