from setuptools import setup, find_packages
setup(
    name="quilt-canary-port",
    version="0.1.0",
    description="Polyformalism canary reference implementations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Casey / SuperInstance",
    packages=find_packages(),
    python_requires=">=3.8",
)
