"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='points-federated',  # Required
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',  # Required
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='tensorflow_federated, setuptools, development',  # Optional
    package_dir={'': 'tensorflow_federated'},  # Optional
    packages=find_packages(where='tensorflow_federated'),  # Required
    python_requires='>=3.6, <4',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["rsa~=4.6.0",
                      "absl-py~=0.10.0",
                      "attrs~=18.2",
                      "cachetools~=3.1.1",
                      "dm-tree~=0.1.1",
                      "enum34~=1.1",
                      "grpcio~=1.29.0",
                      "grpcio-tools~=1.29.0",
                      "gmpy2~=2.0.8",
                      "h5py~=2.6",
                      "numpy~=1.18.0",
                      "pandas~=0.24.0",
                      "portpicker~=1.3.1",
                      "retrying~=1.3.3",
                      "six~=1.12.0",
                      "tensorflow~=2.3.0",
                      "tensorflow-model-optimization~=0.1.3",
                      "tensorflow-privacy~=0.2.0",
                      "tensorflow-addons~=0.8.0",
                      "tensorflow_datasets~=2.0.0",
                      "typing~=3.7.0",
                      "pyopenssl~=19.1.0",
                      "pycrypto~=2.6.1",
                      "scikit-learn~=0.20.0",
                      "utilitybelt~=0.2.6",
                      "pycrypto~=2.6.1",
                      "pymysql~=0.9.3",
                      "phe~=1.4.0",
                      "SQLAlchemy~=1.3.17",
                      "psutil~=5.7.0",
                      "progressbar~=2.5",
                      "Pillow~=6.2.0",
                      "numba~=0.50.1",
                      "gmssl~=3.2.1",
                      "cryptography~=3.4.7",
                      "pathos~=0.2.7",
                      "pyspark==3.0.1"],
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    include_package_data=True
)