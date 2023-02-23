# Implementation Documentation

## Input / Output

### Input

- The midi files in the Data folder are parsed for notes. Each midi file contains multiple midi tracks, and each track has multiple messages. The notes are extracted from the messages of type "note on." The notes are collected from each track and passed on to the trie to be handled based on the specified depth before moving on to the next track. This is how input is given.

### Output

- The Markov Chain generates a list of 500 notes using the user's specified configurations, such as the depth and prefix notes, and the data from the initialized trie data structure. If the user does not provide prefix notes, then the prefix notes are randomly generated for the user.

## Complexity

Trie Class has the space complexity of O(N*k), where N is number of nodes in the trie, each node has a pointer to the next unique note, and k is the total number of unique sequences of notes. Trie is constructed in a traditional way, so space complexity doesn't differ.


## Class diagram

The diagram for the class structure of the project.
![image](https://user-images.githubusercontent.com/77237218/218267397-7882014c-5d68-44e4-85a6-cfb1b90f221e.png)

## Possible improvement

May be better names for the functions and variables. Overall more readable code.
