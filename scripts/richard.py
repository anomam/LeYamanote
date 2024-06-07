from leyamanote.cifar10 import Cifar10Repository


DIR_DATA = "/Users/marco/workspace/leyamanote/data/cifar10/"


def main() -> None:
    # download and extract cifar10 data
    repo = Cifar10Repository(folder=DIR_DATA)
    fp = repo.download()
    repo.extract(fp)
    # load data from first batch
    idx = 0
    fp_batch = repo.fp_train_batch(idx)
    data = repo.load_batch(fp_batch)
    print(data.X.shape)


if __name__ == "__main__":
    main()
