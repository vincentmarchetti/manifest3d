# manifest3d
Python code to help generate prototype manifests delivering 3D assets using IIIF principles

The scripts use a forked, development branch of the PyPI package iiif-prezi3. 
This Python package depends on the pydantic PyPI package which in Jan 2024 was not the 
most recent version. To get the correct version, use the Python pip module to install the
standard iiif-prezi3 package, with command

python -m pip install iiif-prezi3

This will also install the correct, earlier versions of dependency packages.

Successfully installed Pillow-9.5.0 certifi-2023.11.17 charset-normalizer-3.3.2 idna-3.6 iiif-prezi3-1.2.1 pydantic-1.10.13 requests-2.31.0 urllib3-2.0.7
