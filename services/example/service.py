import logging

from connectors.some import call

logger = logging.getLogger(__name__)


def main():
    logger.info(f"Run {__name__}.main")
    call()
