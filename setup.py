
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

description='PhishyAI trains ML models for Phishy, a Gmail extension which leverages ML to detect phishing attempts in all incoming emails'
setup(  
    name='phishyAI',
    python_requires='>3.1.1',
    version='0.1',
    description=description,
    author='Khalid Alam',
    author_email='kalam034@uottawa.ca',
    include_package_data=True,
    url='https://github.com/kalam034/phishy',
    license='MIT',
    install_requires=requirements,
    scripts=['run_pipeline.py'],
    packages=find_packages(where="src")
    )

			