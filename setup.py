from setuptools import setup, find_packages

setup(
    name='work_directory',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Remove outliers from dataframe using interqurtile range',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/RamyGendy/myworkspacepackages',
    author='Ramy Gendy',
    author_email='Ramy.gendy@outlook.com'
)