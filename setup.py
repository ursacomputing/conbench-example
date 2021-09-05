import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()


setuptools.setup(
    name="example",
    version="0.0.0",
    description="Example project using Conbench",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    maintainer="Apache Arrow Developers",
    maintainer_email="dev@arrow.apache.org",
    url="https://github.com/ursacomputing/conbench-example",
    install_requires=[],
)
