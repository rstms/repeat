"""repeat - a redundant pipe fitting

A packaged CLI program

"""
from .context import Context
from .exception import ParameterError
from .constant import status
from .cli import cli
from .version import __version__, __timestamp__, __buildinfo__, __header__

__all__ = ['Context' 'ParameterError', 'status', 'cli', '__version__']
