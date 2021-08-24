# {{ project.name }} - {{ project.description.short }}

{{ project.description.medium }}

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
pip install {{ project.name }}
```

Optionally, install the dev/test modules:
```
pip install {{ project.name }}[dev]
```

------
## Module Dependencies
install:
```{% for module in project.modules.install %}
{{ module }}{% endfor %}
```

test:
```{% for module in project.modules.test %}
{{ module }}{% endfor %}
```

dev:
```{% for module in project.modules.dev %}
{{ module }}{% endfor %}
```

------
## Usage:
```
{{ project.usage }}
```

