from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='CogEnvDecoder',
    version='0.0.1',
    packages=setuptools.find_packages(),
    url='https://github.com/1019388642/UnityEnvDataDecoder',
    license='MIT',
    author='Example Author',
    author_email='author@example.com',
    description='A small example package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
