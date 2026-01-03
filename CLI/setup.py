from setuptools import setup, find_packages

setup(
    name="myfastlib",
    version="1.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "myfast=myfastlib.cli.main:main"
        ]
    },
    author="Your Name",
    description="High-performance Python utility library",
    python_requires=">=3.8",
)
