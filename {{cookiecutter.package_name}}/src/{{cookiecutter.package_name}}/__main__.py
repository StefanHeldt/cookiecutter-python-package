import logging.config

from template_python_package.logging import LOGGING_CONFIG


logger = logging.getLogger("template_python_package")


def main() -> None:
    logging.config.dictConfig(LOGGING_CONFIG)
    logger.info("Starting...")


if __name__ == "__main__":
    main()
