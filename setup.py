from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    author_email='adam@operatingops.org',
    author='Adam Burns',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    description="Provides a decorator that implements terraform's external program protocol for data sources.",
    extras_require={'test': ['tox==3.5.2']},
    install_requires=['future>=0.16.0'],
    long_description=readme(),
    name='terraform_external_data',
    packages=['terraform_external_data'],
    url='https://github.com/operatingops/terraform_external_data',
    version='0.0.5'
)
