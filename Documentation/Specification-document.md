# Specification document

I have knowledge of the mighty Python Programming language
Bachelor of Science in Computer Science (Tietojenkäsittelytieteen kandidaatti TKT)

## Introduction

My project aims to generate music using a MIDI dataset. The process involves:

- Parsing the contents of MIDI files
- Content would be notes and possibly frequencies
- Inputting them into a Markov Chain
- Storing notes and their frequencies in a Trie structure
- Retrieving the proceeding notes of a given note
- Using the Markov Chain algorithm to generate new music based on the patterns in the notes stored in the Trie.
- Time and space complexity objective would be O(n) with Trie data structure

## Tools and Libraries

- Python programming language
- `mido`, `midiutil`, `pretty_midi`, `midi2audio` or `fluidsynth` for working with MIDI files and soundfonts
- `click` for the user interface.

## User Interface

The user interface will have the following features:

- The ability to generate a MIDI file
- The ability to play the generated MIDI file

## Sources

### For Markov Chain

- [Datacamp - Markov Chain](https://www.datacamp.com/tutorial/markov-chains-python-tutorial)
- [Wikipedia - Markov Chain](https://www.wikiwand.com/en/Markov_chain#introduction)

### For Trie

- [Tutorialpoint - Trie](https://tutorialspoint.dev/data-structure/advanced-data-structures/trie-insert-and-search)
- [wikipedia - Trie](https://www.wikiwand.com/en/Trie)
- [Javatpoint - Trie](https://www.javatpoint.com/trie-data-structure)
