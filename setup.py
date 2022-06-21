import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='batch-requests',
    version='0.1.2',
    scripts=[],
    author="apinanyogaratnam",
    author_email="apinanapinan@icloud.com",
    description="make batch http requests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apinanyogaratnam/batch-requests",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aiohttp',
        'setuptools',
        'wheel',
        'tqdm',
        'twine',
    ]
)
