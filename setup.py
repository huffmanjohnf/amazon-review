import os

from setuptools import find_packages, setup

PATH_ROOT = os.path.dirname(__file__)


def load_requirements(path_dir=PATH_ROOT):
    with open(os.path.join(path_dir, "requirements.txt"), "r") as file:
        lines = [ln.strip() for ln in file.readlines()]
    return lines


setup(
    name="amazon_review",
    version="0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=load_requirements(PATH_ROOT),
    entry_points={"console_scripts": ["train=amazon_review.cli:app", "client=amazon_review.client:app"]},
)
