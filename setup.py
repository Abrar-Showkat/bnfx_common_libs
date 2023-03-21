from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='bnfx_common_libs',
    version='0.0.2',
    author='Abrar Showkat',
    author_email='abrarshowkat@yahoo.com',
    description='Package for bnfx',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mike-huls/toolbox',
    project_urls={
        "Bug Tracker": ""
    },
    license='MIT',
    packages=find_packages(),
    install_requires=['kafka-python', 'urllib3'],
)
