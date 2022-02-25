from setuptools import setup
setup(
    name = 'youtube',
    version = '0.1.0',
    packages = ['youtube'],
    entry_points = {
        'console_scripts': [
            'youtube = extension.__main__:parser'
        ]
    })