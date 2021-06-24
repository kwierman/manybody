from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
    'abc', # Needed for abstract base classes
    'xgboost'
]

setup(
    name='manybody',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="MLOps Design Patterns for Many Bodies",
    license="MIT",
    author="Kevin Wierman",
    author_email='kwierman@gmail.com',
    url='https://github.com/kwierman/manybody',
    packages=['manybody'],
    install_requires=requirements,
    keywords='manybody',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
