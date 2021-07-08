import importlib
import argparse
import logging
import config  # noqa: чтобы работал logger

logger = logging.getLogger(__name__)


def runner(service: str):
    try:
        module = importlib.import_module(f"services.{service}.service")
    except ImportError:
        logger.warning(f"No module {service} found.")
    else:
        module.main()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Choose service to start.')
    parser.add_argument('service', metavar='S', type=str, nargs='?', help='Choose service to start')

    args = parser.parse_args()
    runner(args.service)
