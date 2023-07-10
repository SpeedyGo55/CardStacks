from setuptools import setup
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="CardStacks",
    version="0.1.1",
    description="A simple library for creating and manipulating stacks of cards.",
    url="https://github.com/SpeedyGo55/CardStacks",
    author="SpeedyGo55",
    author_email="SpeedyGo55@outlook.com",
    license="GPLv3",
    packages=["CardStacks"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment :: Board Games",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="cards cardstacks cardstack cardstackslib cardstackslibrary cardstackslibrarypython",
    python_requires=">=3",
    project_urls={
        "Bug Reports": "https://github.com/SpeedyGo55/CardStacks/issues",
        "Source": "https://github.com/SpeedyGo55/CardStacks"
    },
)
