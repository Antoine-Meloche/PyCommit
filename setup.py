from setuptools import setup

setup(
    name = "PyCommit",
    version = "0.1.0",
    packages = ['pycommit'],
    entry_points = {
        'console_scripts': [
            'pycommit = pycommit.__main__:main'
        ]
    }
)