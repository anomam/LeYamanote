import pytest

from leyamanote.cifar10 import Cifar10Repository


def test_fp_train_batch(repo: Cifar10Repository) -> None:
    """It's not just about the happy path!"""
    with pytest.raises(ValueError, match="index is incorrect"):
        repo.fp_train_batch(0)


@pytest.mark.parametrize("wrong_idx", [0, 6])
def test_fp_train_batches(wrong_idx: int, repo: Cifar10Repository) -> None:
    """It's not just about the happy path!"""
    with pytest.raises(ValueError, match="index is incorrect"):
        repo.fp_train_batch(wrong_idx)
