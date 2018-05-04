# License MIT

import os
from setuptools import setup  # ,find_packagesD

DISTRO_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def extract_requiremens(file):
    """
    Extracts requirements from file

    :param file: path to file
    :return: list[str] -- list of requirements
    """

    with open(file, 'r') as file:
        return file.read().splitlines()


setup(
    name='supertool-distro',
    version='0.1',
    description='super-super tool',
    author='Olya Nosova',
    author_imail='olenka-nosova@mail.ru',
    license='MIT',
    classifiers=[
        'Topic :: Education'
        'Programming Language :: Python :: 3.6',
    ],
    packages=['supertool'],
    install_requires=extract_requiremens(os.path.join(DISTRO_ROOT_PATH, 'requirements', 'base.txt')),
    test_requires=extract_requiremens(os.path.join(DISTRO_ROOT_PATH, 'requirements', 'test.txt')),
    test_suite='nose.collector',
    scripts=[os.path.join('bin', 'similar_files')],
    bin=[os.path.join('bin', 'similar_files')]
)
