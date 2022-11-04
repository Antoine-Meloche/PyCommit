from setuptools import setup

setup(
    name="PyCommit",
    version="1.0.0",
    author="Antoine Meloche",
    author_email="53838501+Antoine-Meloche@users.noreply.github.com",
    url="https://github.com/Antoine-Meloche/PyCommit",
    description="A simple CLI to create uniform commits",
    license="GPL-3.0",
    packages=['pycommit'],
    entry_points={
        'console_scripts': ['pycommit = pycommit.__main__:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    keywords="commit python py package git pycommit",
    install_requires=[
        "GitPython>=3.1.26"
    ],
    zip_safe=False,
)
