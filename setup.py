import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_utility_functions",
    version="1.0.7",
    author="Daniel Mensing",
    author_email="daniel.mensing@gmx.net",
    description="Utility funtions in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daniel-men/python_utility_functions",
    packages=setuptools.find_packages(),
    install_requires=[
        'opencv-python',
        'pillow',
        'pydicom',
        'numpy',
        'matplotlib',
        'lmdbm'
    ]    
)