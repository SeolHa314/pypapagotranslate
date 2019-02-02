from setuptools import setup

with open("README.md") as rm:
    long_description = rm.read()

setup(
    name = "pypapagotranslate",
    version = "0.1.1.2",
    packages = ["pypapagotranslate",],
    license = "MIT",
    url = "https://github.com/SeolHa314/pypapagotranslate",
    python_requires = ">=3.5",
    platforms = ['Windows', "Linux", "OSX"],
    description = "Papago Translate client for Python",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = "papago translate wrapper n2mt smt",
    install_requires = [
        "requests"
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        "Topic :: Text Processing :: Linguistic",
        "Intended Audience :: Developers"
    ]
)