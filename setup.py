from setuptools import setup
setup(
    name = 'youtubecli',
    version = '1.0.0',
    packages = ['youtubecli'],
    entry_points = {
        'console_scripts': [
            'youtubecli = youtubecli.__main__:parser'
        ]
    })