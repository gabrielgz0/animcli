from setuptools import setup, find_packages

setup(
    name='animcli',
    version='0.2.1',
    packages=find_packages(),
    install_requires=[
        "ascii_magic==1.6"
    ],
    entry_points={
        'console_scripts': [
            'animcli=animcli.main:main',
        ],
    },
    package_data={
        'animcli': ['gifs/*.gif'],
    },
    include_package_data=True,
    description='Transform a GIF into ascii and animate it in the terminal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='gabrielgz',
)