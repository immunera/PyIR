#!/usr/bin env python
from distutils.core import setup
import sys

install_requires=['tqdm']

if sys.version_info < (3, 9):
    install_requires.append('importlib_resources>=1.3.0')


setup(
    name='crowelab_pyir',
    version='1.6.2',
    description='',
    license='Creative Commons Attribution 4.0',
    author='Sam Day, Andre Branchizio, Jordan Willis, Jessica Finn, Taylor Jones, Sam Schmitz, Luke Myers',
    author_email='samuel.day@vumc.org, andrejbranch@gmail.com, jwillis0720@gmail.com, strnad.bird@gmail.com',
    scripts=['./bin/pyir'],
    install_requires=install_requires,
    packages=['crowelab_pyir'],
    package_dir={'crowelab_pyir': './pyir'},
    package_data={'crowelab_pyir': ['data/*',
                                'data/bin/*',
                                # 'data/germlines/*',
                                'data/crowelab_data/*',
                                'data/crowelab_data/*/*',
                                'data/crowelab_data/*/*/*',
                                'data/germlines/aux_data/*',
                                'data/germlines/internal_data/*',
                                'data/germlines/internal_data/*/*'
                                    ]
                  },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
)
