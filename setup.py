from setuptools import setup
setup(
    name = 'youtube',
    version = '1.0.0',
    packages = ['youtube'],
    entry_points = {
        'console_scripts': [
            'youtube = youtube.__main__:parser'
        ]
    })