from setuptools import setup

setup(
    name='linea',
    version='0.1',
    py_modules=['app'],
    install_requires=[
        'Click',
        'Requests'
        ],
    entry_points='''
        [console_scripts]
        linea=app:cli
    ''',
    )
