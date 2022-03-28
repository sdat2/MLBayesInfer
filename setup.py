from setuptools import find_packages, setup

setup(
    name="src",
    version="0.0.1",
    author="sdat2",
    author_email="sdat2@cam.ac.uk",
    description="Part II Computer Science Course Code",
    url="https://github.com/sdat2/MLBayesInfer",
    packages=find_packages(),
    test_suite="src.tests.test_all.suite",
)
