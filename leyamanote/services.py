from pathlib import Path
from typing import Optional

from leyamanote.cifar10 import Cifar10Repository


def download_and_extract(folder: Optional[Path] = None) -> None:
    c10_repo = Cifar10Repository(folder=folder)
    fp = c10_repo.download()
    c10_repo.extract(fp)
