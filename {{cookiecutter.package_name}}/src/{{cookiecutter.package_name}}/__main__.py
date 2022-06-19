import logging.config

from {{cookiecutter.package_name}}.logging import LOGGING_CONFIG


logger = logging.getLogger("{{cookiecutter.package_name}}")


def main() -> None:
    logging.config.dictConfig(LOGGING_CONFIG)
    logger.info("Starting...")


if __name__ == "__main__":
    """{{cookiecutter.friendly_name}}"""
    main(prog_name="{{cookiecutter.project_name}}")
