# Music Gen 1.0

![Music notes](https://github.com/astranero/music-generator/blob/main/Documentation/png_image2.png)

[*Music Notes PNGs by Vecteezy*](https://www.vecteezy.com/free-png/music-notes)

## Introduction

Music Generator 1.0 is a project where Markov Chain and Trie Data Structure has been implemented to generate music both as mav file and midi file.
Generator can also play the generated mav file using pygame mixer.

## Installation and Instructions

This project is using python 3.10 and poetry version 1.4.0, which needs to be installed.

Fluidsynth has to be installed for project  to work.

`sudo apt-get install fluidsynth`

You will also need .env file in the root directory:

```
# Soundfont path from the root
SOUNDFONT = "<name of a soundfont file>"
# Path from the root to the data folder
DATA_PATH = "/Data/"
```
If you are using a soundfont, then you will need to specify it in the .env file as a variable _SOUNDFONT_.

_DATA_PATH_ Variable is the location of a data that needs to be inserted in to the trie for generation of melody.

- Install poetry: `pip install poetry`
- Activate env: `poetry shell`
- Dependency installation: `poetry install`
- Start the project: `poetry run invoke start`
- Run tests: `poetry run invoke test`
- Run pylint: `poetry run invoke lint`

## Links

[Weekly reports](https://github.com/astranero/music-generator/blob/main/Documentation/Weekly_reports.md)

[Specification Document](https://github.com/astranero/music-generator/blob/main/Documentation/Specification-document.md)

[Implementation Document](https://github.com/astranero/music-generator/blob/main/Documentation/Implementation-document.md)

[Testing Document](https://github.com/astranero/music-generator/blob/main/Documentation/Testing-document.md)
