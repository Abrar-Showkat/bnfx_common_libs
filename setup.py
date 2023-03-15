import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name='bnfx_common_libs',
    version='0.0.1',
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
    packages=['toolbox'],
    install_requires=['kafka-python', 'urllib3'],
)
