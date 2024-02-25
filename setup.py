from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']), # include all packages in['mypackage'],
    url='https://github.com/yourgithubusername/mypackage',
    license='MIT',
    author='Your Name',
    author_email='youremail',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    )

