from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    ld = fh.read()

setup(
    name='JoveToolbox',
    version='0.0.1',
    packages=find_packages(),
    scripts=['jtools'],
    install_requires=[
        'requests',
    ],
    author='Noah Wilhoite',
    author_email='notnoah349@gmail.com',
    description='A python and shell utility with all-in-one!',
    license='MIT',
    keywords='python, shell, utility, jove, jove-toolbox, jove-tool-box, multpurpose, community resources',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    
    long_description=ld,
    long_description_content_type='text/markdown',
)
