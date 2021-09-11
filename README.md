# {{ name }} - {{ description_short }}

{{ description_medium }}

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
pip install {{ name }}
```

Optionally, install the dev/test modules:
```
pip install {{ name }}[test]
```

------
## Module Dependencies
install:
```{% for module in modules_install.split(',') %}
{{ module }}{% endfor %}
```

test:
```{% for module in modules_test.split(',') %}
{{ module }}{% endfor %}
```

dev:
```{% for module in modules_dev.split(',') %}
{{ module }}{% endfor %}
```

------
## Usage:
```
{{ usage }}
```

