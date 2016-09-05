import setuptools
import pypandoc

# Use README.md to generate the long_description rather than write rst.
# See https://github.com/pypa/pypi-legacy/issues/148#issuecomment-227757822
long_description = pypandoc.convert('README.md', 'rst')

setuptools.setup(
    name = 'hetio',
    version = '0.2.0',
    author = 'Daniel Himmelstein',
    author_email = 'daniel.himmelstein@gmail.com',
    url = 'https://github.com/dhimmel/hetio',
    description = 'Hetnets in Python',
    long_description=long_description,
    license = 'CC0 1.0',
    packages = ['hetio'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
