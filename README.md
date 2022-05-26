# Practice repository

Playing tutorials from [PyTorch](https://pytorch.org/tutorials/).

# Prerequisite

## Version

```bash
$ python --version
Python 3.9.12
```

## Dependency

Please install by below:

```bash
$ python -m pip install -r requirements.txt
```

# Testing 

Testing flow was builded by [pytest](https://docs.pytest.org/en/7.1.x/contents.html) and configuration ad `./pyproject.toml`

## Usage

Run `make test` in terminal if your os support `make`, or try the command of `test` section in `./Makefile`.

```bash
$ make test
or
$ python -m pytest
...
# test report will show here
```