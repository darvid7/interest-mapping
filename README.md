# Interest Engine

WIP engine to determine what interests should be mapped to what careers.

## Approaches

Currently trying `Google's tensorflow word2vec`.

Read [this for an explanation](https://github.com/darvid7/interest-engine/Explanation.md).

## Installation

1. Activate virtual environment.

`$ source venv/bin/activate`

2. Install Tensorflow for python3.

`$ pip3 install --upgrade tensorflow`

3. Verify Tensorflow installed in virtual environment.

`$ python`

`>>> import tensorflow as tf`

`>>> quit()`

4. Deactivate virtual environment.

`$ deactivate`

## Usage

Assuming you are in the root directory of the git repo.

1. Activate virtual environment.

`$ source venv/bin/activate`

2. Run script.

`$ python3 test.py`

3. When finished deactivate virtual environment.

`$ deactivate`

## Installing other packages

1. Activate virtual environment.

`$ source venv/bin/activate`

2. Install package using pip3.

`$ pip3 install package name`

3. When finished deactivate virtual environment.

`$ deactivate`

## Todo

- speed up computation using GPU

- fix KeyError
