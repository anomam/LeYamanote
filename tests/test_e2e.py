from leyamanote.cifar10 import Cifar10Repository


def test_can_download_data() -> None:
    repo = Cifar10Repository()
    repo.download()
