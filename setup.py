from setuptools import setup, find_packages

setup(
    name='animecli',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'animecli=animecli.main:main',
        ],
    },
    package_data={
        'animecli': ['gifs/*.gif'],
    },
    include_package_data=True,
    description='Transform a GIF into ascii and animate it in the terminal',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    author='gabrielgz',
    #author_email='',
    #url='https://github.com/seuusuario/meu_modulo',
    # classifiers=[
    #     'Programming Language :: Python :: 3',
    #     'License :: OSI Approved :: MIT License',
    # ],
)
