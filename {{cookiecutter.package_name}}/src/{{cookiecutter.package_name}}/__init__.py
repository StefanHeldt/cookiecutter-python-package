import os
from pathlib import Path

from pkg_resources import DistributionNotFound
from pkg_resources import get_distribution

package_root = Path(__file__).resolve(strict=True).parents[2]
log_path = package_root.joinpath("logs")

if not os.path.exists(log_path):
    os.makedirs(log_path)

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "template_python_package"
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound
