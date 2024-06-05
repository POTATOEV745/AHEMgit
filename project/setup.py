from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        #required imports below:
        #tkinter
        #PIL
        #time
    ],
    entry_points={
        'console_scripts': [
            'my_project=my_project.main:main',
        ],
    },
    author='Evan',
    author_email='evanveryguud@gmail.com',
    description='software for AHEMSyS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://https://github.com/POTATOEV745/AHEMSYS1',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
