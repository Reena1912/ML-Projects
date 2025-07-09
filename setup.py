from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements,
    excluding '-e .' and comments.
    """
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()  # Remove leading/trailing whitespace
            if not line or line.startswith("#"):
                continue  # Skip blank lines and comments
            if line.startswith("-e "):  # Skip editable installs like '-e .'
                continue
            requirements.append(line)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Asher',
    author_email='reenarao1912@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
