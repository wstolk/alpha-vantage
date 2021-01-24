import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

packages = ['alpha_vantage']

requires = [
    'requests>=2'
]

test_requirements = []

about = {}
with open(os.path.join(here, 'alpha_vantage', '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    packages=find_packages(),
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'alpha_vantage': 'alpha_vantage'},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=requires,
    license=about['__license__'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    project_urls={
        'Source': 'https://github.com/wstolk/vantage_py',
    },
)
