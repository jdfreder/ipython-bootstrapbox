# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup
try:
    from ipythonpip import cmdclass
except:
    cmdclass = lambda *args: None

setup(
    name='bootstrapbox',
    version='0.1',
    description='Bootstrap grid layout widgets.',
    author='Jonathan Frederic',
    author_email='jon.freder@gmail.com',
    license='New BSD License',
    url='https://github.com/jdfreder/ipython-bootstrapbox',
    keywords='python ipython javascript bootstrap flex box responsive bootstrapbox widget',
    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python',
                 'License :: OSI Approved :: MIT License'],
    packages=['bootstrapbox'],
    include_package_data=True,
    install_requires=["ipython-pip"],
    cmdclass=cmdclass('bootstrapbox'),
)
