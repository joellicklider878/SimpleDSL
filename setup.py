from setuptools import setup, find_packages

setup(
    name='SimpleDSL',
    version='1.0.0',
    description='A domain-specific language for [describe the purpose of your DSL]',
    author='Joel Licklider',
    author_email='joellicklider@gmail.com',
    url='https://github.com/joellicklider878/SimpleDSL',
    packages=find_packages(),
    install_requires=[
        'antlr4-python3-runtime==4.9.2',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'simpledsl=yourpackage.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)