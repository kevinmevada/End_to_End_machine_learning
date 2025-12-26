from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, encoding="utf-8") as file_obj:
        requirements = [
            req.strip() for req in file_obj.readlines()
            if req.strip() and req.strip() != HYPHEN_E_DOT
        ]
    return requirements

setup(
    name="mlproject",
    version="0.1.0",
    author="Kevin Mevada",
    author_email="mevadakevin@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.8",
)
