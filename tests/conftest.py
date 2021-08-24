# pytest fixtures

import pytest

from pathlib import Path


@pytest.fixture()
def project():
    return Path().absolute().stem
