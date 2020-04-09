from setuptools import setup

# Run the following to create a new predictor deployment artifact
# python setup.py sdist --format=gztar
setup(
    name='custom_predictor',
    version='0.1',
    scripts=['predictor.py'])
