from setuptools import setup

setup(
    name="masonite-cli",
    version='0.20',
    py_modules=['craft'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        craft=craft:group
        craft-vendor=craft:cli
    ''',
)
