import tarfile
from pathlib import Path
from typing import Optional

import requests

from leyamanote import DIR_DATA, LOGGER


DIR_CIFAR10 = DIR_DATA / "cifar10/"


class Cifar10Repository:
    url = "http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
    tar_filename = "cifar-10-python.tar.gz"
    subfolder_name = "cifar-10-batches-py"
    classes = ["plane", "car", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

    def __init__(self, folder: Optional[Path] = None) -> None:
        self._folder = folder or DIR_CIFAR10

    def download(self) -> Path:
        LOGGER.info(f"Downloading dataset into '{self._folder}'")
        fp = self._folder / self.tar_filename
        if not fp.exists():
            self._folder.mkdir(exist_ok=True, parents=True)
            with requests.get(self.url) as resp:
                resp.raise_for_status()
                with fp.open("wb") as f:
                    f.write(resp.content)
        LOGGER.info(f"Finished downloading cifar10 dataset '{self._folder}'")
        return fp

    def extract(self, fp: Path) -> None:
        LOGGER.info(f"Unzipping '{fp}'")
        with tarfile.open(fp) as f:
            f.extractall(fp.parent)
        LOGGER.info(f"Done unzipping '{fp}'")

    def fp_train_batch(self, idx: int) -> Path:
        if not (1 <= idx <= 5):
            raise ValueError(f"Batch index is incorrect: '{idx}'")
        return self._folder / self.subfolder_name / f"data_batch_{idx}"

    @property
    def fp_test_batch(self) -> Path:
        return self._folder / self.subfolder_name / "test_batch"
