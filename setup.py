from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='weixin_en2zh',
      version=version,
      description="weixin api",
      long_description=open('README.rst').read().strip(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='weixin webchat',
      author='timger',
      author_email='haibolib@gmail.com',
      url='http://www.timger.info/about',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      scripts = ['scripts/weixin_en2zh.py'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
