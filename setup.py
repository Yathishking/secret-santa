from setuptools import setup, find_packages
from pathlib import Path

# Get the current directory
current_dir = Path(__file__).parent

requirements_path = '/home/yathish/Desktop/Python/Secret_Santa/requirements.txt'
with open(requirements_path, 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='SecretSantaApp',
    version='1.0.0',
    author='Yathish',
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=requirements,
    description='A Secret Santa assignment application',
    scripts=['main.py'],
    entry_points={
        'console_scripts': [
            'secretsanta=main:main',
        ],}


)
