import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="native_shortuuid", # Replace with your own username
    version="0.0.1",
    author="foundertherapy",
    author_email="laith@foundertherapy.co",
    description="A decoder/encoder library for uuid",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucidgreen/native_shortuuid",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)