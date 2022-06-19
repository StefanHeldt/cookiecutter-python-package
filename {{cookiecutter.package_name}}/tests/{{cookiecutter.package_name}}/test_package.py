import toml
from {{cookiecutter.package_name}} import __version__


def test_package():
    config: dict = toml.load("pyproject.toml")
    assert config["tool"]["poetry"]["version"] == __version__
