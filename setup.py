from setuptools import setup, find_packages

setup(
    name='prettier_prints',
    packages=find_packages(include=['prettier_prints']),
    version='0.1.0',
    description='colored outputs library for easier readability and styling',
    author='Dylan Stocking',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',
)
