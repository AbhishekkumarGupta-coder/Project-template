from setuptools import find_packages, setup

setup(
    name="qasystem",
    version="0.0.1",
    author="Abhishek Kumar Gupta",
    author_email="vicky03867@gmail.com",
    packages=find_packages(),  # This should find all packages in the directory
    install_requires=["langchain"],
)
