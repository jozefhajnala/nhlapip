import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nhlapip",
    version="0.0.1",
    author="Jozef Hajnala",
    author_email="jozef.hajnala@gmail.com",
    description="A minimum-dependency Python interface to the NHL API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jozefhajnala/nhlapip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)