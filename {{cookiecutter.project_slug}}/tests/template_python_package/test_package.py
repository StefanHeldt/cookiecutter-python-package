import toml
from template_python_package import __version__


def test_package():
    config: dict = toml.load("pyproject.toml")
    assert config["tool"]["poetry"]["version"] == __version__
