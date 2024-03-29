import setuptools
# setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colorprt",
    version="3.0.2",
    author="MichaelZhou",
    author_email="zyqing601@163.com",
    description="It's a simple tools to print colorfully. Easy to use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Michaelzhouisnotwhite/Colorprt",
    project_urls={
        "Bug Tracker": "https://github.com/Michaelzhouisnotwhite/Colorprt/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
