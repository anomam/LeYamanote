from pathlib import Path

from leyamanote.cifar10 import Cifar10Repository


DIR_DATA = "/Users/marco/workspace/leyamanote/data/cifar10/"


def main() -> None:
    # download and extract cifar10 data
    repo = Cifar10Repository(folder=Path(DIR_DATA))  # <<< type hints
    fp = repo.download()
    repo.extract(fp)
    # load data from first batch
    idx = 1  # <<< raise exception, and unit test + parametrizatio
    fp_batch = repo.fp_train_batch(idx)
    data = repo.load_batch(fp_batch)
    print(data.X.shape)


if __name__ == "__main__":
    main()
