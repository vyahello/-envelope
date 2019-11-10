# Envelopes matcher
`envelope.py` tool simply checks if envelope one matches envelope two with pure OOP style. Nothing more :)

## Demo
```bash
~ python envelope.py --envelope1 2 2 --envelope2 3 3
2018-06-11 12:18:54,312 INFO Congratulations EnvelopeOne fits into EnvelopeTwo!
~ python envelope.py --envelope1 5 5 --envelope2 4 4
2018-06-11 12:19:08,620 INFO EnvelopeOne does not fit into EnvelopeTwo, please try again! Reason - EnvelopeOne has size 5x5 and EnvelopeTwo has size 4x4
```

## Run unittests
Run `pytest -v` from shell in the root directory of the repository.

## Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all require python packages
