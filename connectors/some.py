import logging

from config import SOME

logger = logging.getLogger(__name__)


def call():
    # сделал warning, чтобы попало в консоль
    logger.warning(f"Call some service with {SOME}")
