from setuptools import setup, find_packages

from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def files_in_folder(folder):
    return [
        (subfolder, [os.path.join(subfolder, file) for file in files])
        for subfolder, _, files in os.walk(folder)
    ]

setup(
    name='tamagotchi',

    version='0.0.1',

    description='Python tamagotchi',
    long_description=long_description,

    url='https://github.com/bitterfly/tamagotchi',

    author='Diana Geneva',
    author_email='dageneva@gmail.com',

    license='GPLv2',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='tamagotchi',

    packages=find_packages(),

    install_requires=['pyxdg'],

    extras_require={
        'dev': [],
        'test': [],
    },

    package_data={

    },

    data_files = files_in_folder('tamagotchi/gui/resources'),

    entry_points={
        'console_scripts': [
            'tamagotchi=tamagotchi.gui.ui:main',
        ],
    },
)
