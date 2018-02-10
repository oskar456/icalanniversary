from setuptools import setup, find_packages


requires = [
    'PyYAML >= 3.12, < 4.0',
    'icalendar >= 4.0.0, < 5.0.0',
    'awesome-slugify >= 1.6.5, < 2.0.0'
]

setup(
    name='icalanniversary',
    version='0.1',
    description='Generate ical files with recurring events of important dates',
    author='Ondřej Caletka',
    author_email='ondrej@caletka.cz',
    license='MIT',
    install_requires=requires,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'icalanniversary = icalanniversary.generator:main',
        ],
    },
)
