from setuptools import setup

setup(
    name = "resizeIcon",
    version = "0.1.0",
    install_requires=[
        "pillow",
        "docopt"
    ],
    tests_require=[
        'pytest',
        "pillow",
    ],
)