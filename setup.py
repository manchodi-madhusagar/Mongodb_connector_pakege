from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.1"
REPO_NAME = "Mongodb_connector_pakege"
PKG_NAME= "mongodb_automation"
AUTHOR_USER_NAME = "manchodi-madhusagar"
AUTHOR_EMAIL = "manchodimadhusagar@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pymongo[srv]>=3.11.3",
        "pandas>=1.1.5",
        "numpy>=1.21.4",
        "tqdm>=4.62.3",
        "PyYAML>=6.0",
        "boto3>=1.18.18",
        "requests>=2.25.1",
        "python-dotenv>=0.19.2",
        "pyarrow>=4.0.1",
        "pymongo",
        "dnspython",
        "ensure",
        "pytest"
    ]
    )



