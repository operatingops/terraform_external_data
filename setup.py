from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    author_email='adam@operatingops.org',
    author='Adam Burns',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only"
    ],
    description="Provides a decorator that implements terraform's external program protocol for data sources.",
    extras_require={'test': ['tox >=3.13, <3.14']},
    long_description=readme(),
    name='terraform_external_data',
    packages=['terraform_external_data'],
    url='https://github.com/operatingops/terraform_external_data',
    version='1.0.1'
)
