# Envelope

## Matching Envelopes
- `envelope.py` tool simply checks if envelope one matches envelope two
```
~ python envelope.py -h
usage: envelope.py [-h] --envelope1 ENVELOPE1 ENVELOPE1 --envelope2 ENVELOPE2
                   ENVELOPE2

This program allows to check if envelope1 fits into envelope2.

optional arguments:
  -h, --help            show this help message and exit
  --envelope1 ENVELOPE1 ENVELOPE1, -en1 ENVELOPE1 ENVELOPE1
                        Size for envelope1 (1x2)
  --envelope2 ENVELOPE2 ENVELOPE2, -en2 ENVELOPE2 ENVELOPE2
                        Size for envelope2 (1x2)
```
## Contributing

### Setup
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vjagello93@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all require python packages

### Run unittests
Run `pytest -v` from shell in the root directory of the repository.