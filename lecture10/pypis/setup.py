from setuptools import setup, find_packages

with open("README.md", "r") as fr:
    long_des = fr.read()

setup(
    name = "demo",
    version="0.1",
    author="NEU",
    description="demo",
    long_description=long_des,
    long_description_content_type = "text/markdown",
    url="http://lxxxxx",
    packages=find_packages(),
    classifiers=[
        "Programming Language:: Python ::3",
        "License :: OSI Approved ::MIT License",
        "Operation System ::OS Independent",
    ],
)