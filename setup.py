# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import restspec

setup(
    name='restspec',
    version=restspec.__version__,
    description="Validate RESTful API intput data using JSON schema.",
    long_description=open("README.md").read(),
    url='http://github.com/theorm/py-restspec',
    license=open("LICENSE").read(),
    author=restspec.__author__,
    author_email='roman@kalyakin.com',
    packages=find_packages(exclude=('tests',)),
    package_data={'': ['LICENSE', '*.md']},
    include_package_data=True,
    install_requires=[
        'jsonschema==2.0.0'
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    tests_require=["nose>=0.10"],
    test_suite = "nose.collector"
)
