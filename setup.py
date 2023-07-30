from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

project_urls = {
    "Homepage": "https://github.com/PhantomLeak/prettier_prints",
    "Bug Tracker": "https://github.com/PhantomLeak/prettier_prints/issues"
}

setup(
    name='prettier_prints',
    packages=find_packages(include=['prettier_prints']),
    version='0.1.0',
    description='colored outputs library for easier readability and styling',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dylan Stocking',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',
    project_urls=project_urls
)