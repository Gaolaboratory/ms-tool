from setuptools import setup, find_packages

setup(
    name="ms-tool",
    version="0.0.1",
    author="Yu (Tom) Gao",
    author_email="yugao@uic.edu",
    description="ms-tool - powerful tools for mass spectrometry data processing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Gaolaboratory/ms-tool",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "lxml",
        "pyarrow",
    ],
    license="Apache-2.0",
    keywords=["mass spectrometry", "proteomics", "mzml", "metabolomics"],
    project_urls={
        "Homepage": "https://github.com/Gaolaboratory/ms-tool",
        "Issues": "https://github.com/Gaolaboratory/ms-tool/issues",
    },
)