from setuptools import setup


version = '0.0.1'


setup(
    name='django-useful-fields',
    version=version,
    url='https://github.com/rmecham/django-useful-fields/',
    author='Rob Mecham',
    description=('Some useful database field definitions for Django.'),
    license='MIT',
    packages=['useful'],
    include_package_data=True,
    zip_safe=False,
    requires=['bleach>=1.4', 'Markdown>=2.6']
)
