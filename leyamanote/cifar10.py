import pickle
import tarfile
from pathlib import Path
from typing import NamedTuple, Optional

import numpy as np
import requests

from leyamanote import DIR_DATA, LOGGER


DIR_CIFAR10 = DIR_DATA / "cifar10/"


class Data(NamedTuple):
    X: np.ndarray
    y: np.ndarray


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

    def extract(self, fp: Path, dest: Optional[Path] = None) -> None:
        LOGGER.info(f"Unzipping '{fp}'")
        destination = dest or fp.parent
        with tarfile.open(fp) as f:
            f.extractall(destination)
        LOGGER.info(f"Done unzipping '{fp}'")

    def load_batch(self, fp_batch: Path) -> Data:
        """Load single batch file:
        - format is pickle
        - each batch has 10000 examples
        - each example image has 3 channels
        - each example is an image of size 32x32 pixels

        If idx is None, will load test batch, otherwise will use
        train batches.
        """

        with fp_batch.open("rb") as f:
            datadict = pickle.load(f, encoding="latin1")
            X: np.ndarray = datadict["data"]
            y: np.ndarray = np.array(datadict["labels"])
            X = (
                X.reshape(10000, 3, 32, 32)  # correct formatting
                .transpose(0, 2, 3, 1)  # reorganize the channels
                .astype("float")  # because int8 otherwise
            )
        return Data(X, y)

    def fp_train_batch(self, idx: int) -> Path:
        if not (1 <= idx <= 5):
            raise ValueError(f"Batch index is incorrect: '{idx}'")
        return self._folder / self.subfolder_name / f"data_batch_{idx}"

    @property
    def fp_test_batch(self) -> Path:
        return self._folder / self.subfolder_name / "test_batch"
