# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md', 'r') as f:
    readme = f.read()
with open('CHANGES', 'r') as f:
    history = f.read()

setup(
    name="aic-modules",
    version="1.0.0",
    description='',
    long_description=readme + '\n\n' + history,
    author="Johan Andersson",
    author_email="Grokzen@gmail.com",
    maintainer='Johan Andersson',
    maintainer_email='Grokzen@gmail.com',
    license='MIT',
    packages=['aic_modules'],
    url='http://github.com/grokzen/aic-modules',
    entry_points={
        'aic.modules': [
            'hostname = aic_modules.hostname:Hostname',
        ],
    },
    install_requires=[],
    classifiers=(
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    )
)
