#!/usr/bin/env python

from setuptools import setup

REQUIRES = []
def read_requirements(file):
    with open(file) as f:
        for line in f:
            line, _, _ = line.partition('#')
            line = line.strip()
            if ';' in line:
                requirement, _, specifier = line.partition(';')
                for_specifier = EXTRAS.setdefault(':{}'.format(specifier), [])
                for_specifier.append(requirement)
            else:
                REQUIRES.append(line)

try:
    read_requirements('requirements.txt')
except FileNotFoundError:
    read_requirements('colorize_cli.egg-info/requires.txt')

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(name='colorize-cli',
      version='0.0',
      license='MIT',
      description='Highlight matched strings in a text',
      long_description=long_description,
      long_description_content_type="text/x-rst",
      author='Aleksandr Vinokurov',
      author_email="aleksandr.vin@gmail.com",
      url='https://github.com/aleksandr-vin/colorize',
      download_url = 'https://github.com/aleksandr-vin/colorize/archive/v0.0.tar.gz',
      keywords = ['cat', 'colors', 'terminal', 'console', 'logs', 'ascii', 'regex', 'cli'],
      packages=['colorize'],
      install_requires=REQUIRES,
      entry_points = {
        'console_scripts': ['colorize=colorize.cli:main'],
      },
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Information Technology',
          'Topic :: Software Development',
          'Topic :: Home Automation',
          'Topic :: Internet',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: System :: Monitoring',
          'Natural Language :: English',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ],
)
