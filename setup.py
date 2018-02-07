from setuptools import setup, find_packages

setup(
     name = 'data-analysis-python',
     version='0.0.1',
     url='www.github.com/nairgokul70/data-analysis-python',
     license='BSD',
     author= 'Gokul Nair',
     packages=find_packages(),
     install_requires=['PyQt5',
                       'pandas',
                       'sqlalchemy',
                       'nltk',
                       'numpy',
                       'jupyter',
                       'python-twitter'],
     entry_points={},
     extras_require={'dev':['flake8',]},
    )
