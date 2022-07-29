import argparse
import logging.config
import sys

from {{cookiecutter.package_name}}.logs import CONFIG
from {{cookiecutter.package_name}} import __version__
from typing import List

logger = logging.getLogger("{{cookiecutter.package_name}}")


def parse_args(args: List[str]) -> argparse.Namespace:
    """Parse command line arguments and parameters.

    Args:
      args ([str]): command line parameters as list of strings.
    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace.

    """
    parser = argparse.ArgumentParser(
        description="{{cookiecutter.project_short_description}}"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (" + __version__ + ")",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        default=logging.root.level,
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        default=logging.root.level,
        action="store_const",
        const=logging.DEBUG,
    )

    return parser.parse_args(args)


def main() -> None:
    logging.config.dictConfig(CONFIG)
    args = parse_args(sys.argv[1:])
    logger.setLevel(args.loglevel)

    logger.info("Starting...")


if __name__ == "__main__":
    """{{cookiecutter.friendly_name}}."""
    main()
