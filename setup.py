from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='terraform_external_data',
    version='0.0.3',
    author='Adam Burns',
    author_email='adam@operatingops.org',
    description="Provides a decorator that implements terraform's external program protocol for data sources.",
    long_description=readme(),
    packages=['terraform_external_data'],
    url='https://github.com/operatingops/terraform_external_data',
    install_requires=['future==0.16.0'],
    extras_require={'test': ['tox==3.5.2']}
)
