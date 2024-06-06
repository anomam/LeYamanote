from pathlib import Path

import pytest

from leyamanote.cifar10 import Cifar10Repository


@pytest.fixture
def repo(tmpdir) -> Cifar10Repository:
    return Cifar10Repository(folder=Path(tmpdir))
