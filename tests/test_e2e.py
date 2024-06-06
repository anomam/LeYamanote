from pathlib import Path

from leyamanote.services import download_and_extract


def test_can_download_data(tmpdir) -> None:
    """Will take a little while, as downloads the full data"""
    tmp_dir = Path(tmpdir)
    download_and_extract(tmp_dir)
