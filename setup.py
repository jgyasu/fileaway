from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="forganiser",
    version="0.0.1",
    author="Jigyasu",
    author_email="jigyasu@outlook.in",
    description="A nifty tool to sort your messy folders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cheesemaafia/forganiser",
    project_urls={
        "Bug Tracker": "https://github.com/cheesemaafia/forganiser/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['forganiser', 'create_folders', 'down_path', 'header', 'move_files', '__init__'],
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires = ["termcolor"]
)