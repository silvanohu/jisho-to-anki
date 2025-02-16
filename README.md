# jisho-to-anki

# Table of Contents
- [Introduction](#introduction)
- [Features](#features)
  - [Searching and File Creation](#searching-and-file-creation)
- [Usage](#usage)
- [Contributing](#contributing)

# Introduction
jisho-to-anki is a lightweight Python script that helps automate the process 
of adding new Japanese vocabulary to your Anki deck. It scans a `.txt` file for 
Japanese words, queries Jisho's API for definitions, and generates a file that 
can be imported directly into Anki.

As a Japanese learner whenever I encounter new words I tend to 
look up their meaning quickly and, in order to avoid disrupting my reading/
listening/watching experience, I save the words in a note and add them to 
my Anki decks in a later moment.
The problem is that these words tend to pile up pretty quickly, so I made 
this script that partly automates the process of creating new Anki cards, 
all that is left to do is importing the file created!

# Features

## Searching and File Creation
- Reads a `.txt` file containing Japanese words (one word per line).
- Uses Jisho's API to retrieve word meanings.
- Extracts relevant information and formats it for Anki import.
- Generates a ready-to-import file with semicolon-separated values.

# Usage
1. Create a `.txt` file with the words you want to add to Anki, one word per line.
2. Set up a `.env` file with the paths to your input and output files.
3. Run the `app.py` file.
4. Import the generated file into Anki, selecting semicolons (`;`) as separators.

# Contributing
Feel free to contribute in any way!