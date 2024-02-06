from setuptools import setup, find_packages

setup(
    name='unbabel_cli',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pydantic',
        'pytest',
    ],
        entry_points={
        'console_scripts': [
            'unbabel_cli=unbabel_cli.main:main',
        ],
    },
)