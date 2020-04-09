
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

description='Trains a random forest, gradient boost tree and logistic regression model to catch phishing urls'
setup(  
    name='phishy-classifier',
    python_requires='>3.1.1',
    version='1.0',
    description=description,
    author='Khalid Alam',
    author_email='kalam034@uottawa.ca',
    include_package_data=True,
    url='https://github.com/kalam034/phishy',
    license='MIT',
    install_requires=requirements,
    scripts=['src/run_pipeline.py'],
    packages=find_packages(where="src")
    )

			