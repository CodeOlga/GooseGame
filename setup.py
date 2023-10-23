from setuptools import setup

APP = ['./main.py']
DATA_FILES = [
    ('.', [
        'background.png',
        'bonus.png',
        'enemy.png',
        'player.png',
    ]),
    ('Goose', [
        'Goose/1-1.png',
        'Goose/1-2.png',
        'Goose/1-3.png',
        'Goose/1-4.png',
        'Goose/1-5.png',
    ])
]


OPTIONS = {
    'argv_emulation': True,
    'packages': ['pygame'], 
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
