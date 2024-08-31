from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cc.scpi",
    version="2024.8.31",
    author="Uncertainty.",
    author_email="t_k_233@outlook.email",
    description="Wrapper of SCPI language for controlling various lab instruments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uncertainty-cc/SCPI-Python",
    project_urls={
        
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "cc-serializer",
    ],
    package_dir={"": "src/"},
    packages=find_namespace_packages(where="src/", include=["cc.scpi"]),
    python_requires=">=3.8",
)
