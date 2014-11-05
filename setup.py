from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pysparcs',
      version=version,
      description="python scripts to handle NYC sparcs data.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='sparcs',
      author='Yin Aphinyanaphongs, Yu Liang',
      author_email='yin.a@nyumc.org',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
