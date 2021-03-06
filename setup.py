import setuptools

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

with open('readme.org', 'r') as f:
    readme = f.read()

setuptools.setup(
    name="CatFlow",
    version="0.1.0",
    url="https://github.com/SUNCAT-Center/CatFlow",

    author="Jacob Boes",
    author_email="jrboes@stanford.edu",

    description="Fireworks workflows for catalysis applications.",
    long_description=readme,
    license='GPL-3.0',

    packages=[
        'catflow',
    ],
    package_dir={'catflow': 'catflow'},
    install_requires=requirements,
    python_requires='>=3.5, <4',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Chemistry',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
