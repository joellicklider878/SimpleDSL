from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()
    
setup(
    author='Joel Licklider',
    author_email='joellicklider@gmail.com',
    description='A PyPI package with a Markdown README',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='markdown-description-example',
    url='https://github.com/joellicklider878/SimpleDSL',
    version='0.0.1',
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