from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


version = '0.0.3'


setup(
    name='django-useful-fields',
    version=version,
    url='https://github.com/rmecham/django-useful-fields/',
    author='Rob Mecham',
    description='Some useful database field definitions for Django.',
    long_description=long_description,
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'Django>=1.8',
        'bleach>=1.4',
        'Markdown>=2.6',
        'pytz>=2015',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
