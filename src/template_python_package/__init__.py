import os
from pathlib import Path

package_root = Path(__file__).resolve(strict=True).parents[2]
log_path = package_root.joinpath("logs")

if not os.path.exists(log_path):
    os.makedirs(log_path)
