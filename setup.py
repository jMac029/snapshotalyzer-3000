from setuptools import setup

setup(
    name='snapshotalyzer-3000',
    version='0.1',
    author='James McMillan',
    author_email='jmcmillan29@gmail.com',
    description='SnapshotAlyzer 3000 is a tool to manage AWS EC2 snapshots',
    license='MIT',
    packages=['shotty'],
    url='https://github.com/jMac029/snapshotalyzer-3000',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)