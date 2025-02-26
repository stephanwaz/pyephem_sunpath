#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pyephem>=3.7.6.0', 'skyfield']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

package_data = {'pyephem_sunpath':["de421.bsp"]}

setup(
    author="Santosh Philip",
    author_email='santosh_philip@notemail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Calculate sunpath using pyephem",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyephem_sunpath',
    name='pyephem_sunpath',
    packages=find_packages(include=['pyephem_sunpath']),
    package_data=package_data,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/santoshphilip/pyephem_sunpath',
    version='0.2.1',
    zip_safe=False,
)
