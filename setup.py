import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="selective_linter",
    version="0.0.1",
    author="Matt Boran",
    author_email="mattboran@gmail.com",
    description="A script to be used as a pre-commit git hook for projects written in Swift",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattboran/SelectiveSwiftLinter",
    download_url="https://github.com/mattboran/SelectiveSwiftLinter/releases/download/0.0.1/selective_linter-0.0.1-py3-none-any.whl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'colorama',
        'sh'
    ],
    python_requires='>3.0.0'
)