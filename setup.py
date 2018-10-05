import os
from setuptools import setup, find_packages


def install_requires():
    filepath = os.path.dirname(__file__)
    with open(os.path.join(filepath, 'requirements.txt')) as fobj:
        return fobj.read().splitlines()

setup(
    zip_safe = False,
    name = "messenger-maid-chan",
    version = "0.2",
    packages = find_packages(),
    author='Iskandar Setiadi',
    author_email='iskandarsetiadi@gmail.com',
    url='https://github.com/freedomofkeima/messenger-maid-chan',
    description='Maid-chan feat Facebook Messenger bot',
    license="MIT",
    entry_points = {
        'console_scripts': [
                'maidchan = maidchan.cmds.main:main',
                'maidchan_primitive = maidchan.cmds.primitive_worker:main',
                'maidchan_scheduler = maidchan.cmds.scheduler_worker:main'
            ]
    },
    install_requires = install_requires(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
    ]
)
