from pathlib import Path
from unittest.mock import patch

import pytest

from leyamanote.cifar10 import Cifar10Repository
from leyamanote.services import download_and_extract


DIR_FIXTURE = Path(__file__).parent / "fixtures"


def test_fp_train_batch(repo: Cifar10Repository) -> None:
    """It's not just about the happy path!"""
    with pytest.raises(ValueError, match="index is incorrect"):
        repo.fp_train_batch(0)


@pytest.mark.parametrize("wrong_idx", [0, 6])
def test_fp_train_batches(wrong_idx: int, repo: Cifar10Repository) -> None:
    """It's not just about the happy path!"""
    with pytest.raises(ValueError, match="index is incorrect"):
        repo.fp_train_batch(wrong_idx)


FP_TO_EXTRACT = DIR_FIXTURE / "fixture.tar.gz"


def test_download_and_extract(tmpdir) -> None:
    destination = Path(tmpdir)
    assert not any(destination.iterdir()), "destination folder is not empty"
    with patch.object(Cifar10Repository, "download", return_value=FP_TO_EXTRACT):
        download_and_extract(folder=destination)
    dest_dirs = list(destination.iterdir())
    assert any(dest_dirs), "destination folder is empty, file were not extracted"
