from leyamanote.cifar10 import Cifar10Repository


def test_can_download_file(tmpdir, repo: Cifar10Repository) -> None:
    repo.download()
