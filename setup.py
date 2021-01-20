from setuptools import find_packages, setup

setup(
    name='giniustk',
    version='0.0.2',
    description='Ginius ToolKit',
    author='Ruben Rosino',
    author_email='ruben.rosino@mercadolibre.com',
    url='https://github.com/rrubens/modelsUtils',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development',
    ],
    tests_require=[
        'pytest',
    ]
)