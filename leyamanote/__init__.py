import logging
from pathlib import Path


# some logging
LOGGER = logging.getLogger(__name__)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
LOGGER.addHandler(handler)

LOGGER.setLevel(logging.DEBUG)

# some config params
DIR_ROOT = Path(__file__).parent.parent
DIR_DATA = DIR_ROOT / "data"
