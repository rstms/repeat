# repeat - a redundant pipe fitting

Copy input to output until EOF then repeat the output stream one or more times.

## Example
```
$ echo -e "one\ntwo\nthree" | repeat
one
two
three
one
two
three
```
------
## Installation

Install with pip:
```
 pip install repeat
```

Optionally, install the dev/test modules:
```
pip install repeat[dev]
```

------
## Module Dependencies
install:
```
click
```

test:
```
pytest
pytest-click
tox
```

dev:
```
bumpversion
twine
yapf
j2cli
sphinx
sphinx-click
sphinx-rtd-theme
sphinx-serve
```

------
## Usage:
```
INSERT_CLI_USAGE_HERE
```

