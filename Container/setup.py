import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="ddnMath",
    version="0.0.1",
    author="Davoud Nasrabadi",
    author_email="davoud.nasrabadi@gmail.com",
    description="a small mathematics library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davoudnasrabadi/ddnmath",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python ::3",
        "License :: OSI Approved :: MIT license",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)
