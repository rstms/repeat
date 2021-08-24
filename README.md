# {{ project.name }} - {{ project.description.short }}

{{ project.description.medium }}


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
```
{% for module in project.modules.install %}{{ module }}
{% endfor %}
```

dev/test:
```
{% for module in project.modules.dev %}{{ module }}
{% endfor %}
```

------
## Usage:
```
{{ project.usage }}
```

