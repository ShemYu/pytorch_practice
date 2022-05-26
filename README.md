# Practice repository

Playing tutorials from [PyTorch](https://pytorch.org/tutorials/).  Building testing process for tutorial codes checking.

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

# Code quality

Using autoreformat module `isort`, `black` which concerned the [PEP8](https://peps.python.org/pep-0008/) to increase code quality.

## Usage

Run `make check` to check if their are any coding style problems, `make fix` to fix it automatically.

### Check

```bash
$ make check 
black --check src tests
would reformat src/hello_world.py
would reformat tests/test_hello_world.py

Oh no! 💥 💔 💥
2 files would be reformatted, 2 files would be left unchanged.
```

### Fix

```bash
$ make fix
black src tests
reformatted tests/test_hello_world.py
reformatted src/hello_world.py

All done! ✨ 🍰 ✨
2 files reformatted, 2 files left unchanged.
isort .
Fixing /Users/shemyu/Documents/programing/pytorch_practice/src/hello_world.py
Skipped 1 files
```