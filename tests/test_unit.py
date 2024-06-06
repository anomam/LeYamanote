import pytest

from leyamanote.cifar10 import Cifar10Repository


def test_fp_train_batch() -> None:
    """It's not just about the happy path!"""
    repo = Cifar10Repository()
    with pytest.raises(ValueError, match="index is incorrect"):
        repo.fp_train_batch(0)
