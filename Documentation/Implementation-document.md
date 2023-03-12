# Implementation Documentation

## Input / Output

### Input

- The midi files in the Data folder are parsed for notes. Each midi file contains multiple midi tracks, and each track has multiple messages. The notes are extracted from the messages of type "note on." The notes are collected from each track and passed on to the trie to be handled based on the specified depth before moving on to the next track. This is how input is given.

### Output

- The Markov Chain generates a list of 500 notes using the user's specified configurations, such as the depth and prefix notes, and the data from the initialized trie data structure. If the user does not provide prefix notes, then the prefix notes are randomly generated for the user.

## Complexity

### Time Complexity

#### Markov Chain

In markov chain `insert`method has a time complexity of O(N*M), where N is the length of input notes and M is depth of the trie.
With `_notes_depth_size_sublist` method we have also time complexity of O(N*M), where N is length of the input notes and M is depth of the trie.
`generate_melody` method has a time complexity of O(K*M), where K is the length of melody sequence that needs to be generated and M is the depth
of the trie. So overall time complexity for markov chain is O(K*M), because K is larger than any other factors in the markov chain.


#### Trie

Time complexity of inserting a sequence of notes in the Trie is O(m), and m is the length of sequence of notes. Trie will traverse from a root to the last note of the sequence, if a node with this note doesn't exist then new node with this note will be created. If we are inserting n sequences, then time complexity of insertion would be O(nm), where n is number of sequences of notes.
Time complexity of searching a note that follows a sequence of notes in the trie is also O(m), whre m is the length of the sequence of notes. In this case also we will traverse from the root node to the node of last note of the sequence. 
Time complexity of getting a random note is O(k), where k is the number of children nodes in the parent node. 


### Space Compelexity

#### Markov Chain
In markov chain `insert`method has a space complexity of O(N*M), where N is number of the notes inside a sublist and M is the depth of the trie. 
This is because **sequence** variable stores M sized sequences of notes, and N is number of notes that has been inserted in to `insert` method.
`_notes_depth_size_sublist` has a space complexity of O(N) where N is the number of notes in the **notes** variable, because of yield depth sized notes are not stored. We are generating fixed sized sublist of notes, but returning them to calling function and not storing them. 
The space complexity of `generate_melody` is O(K), where K is the size of the melody sequence that we want to generate.

#### Trie

Each node in trie is a single note and can have on or more child nodes for each following note of the parent nodes note.
So, the space complexity for trie is O(K^N), where K is the number of unique notes (all possible notes that can exist) and N is the depth of the trie (the maximum length of the input sequences).

## Class diagram

The diagram for the class structure of the project.
![image](https://user-images.githubusercontent.com/77237218/218267397-7882014c-5d68-44e4-85a6-cfb1b90f221e.png)

## Possible improvement

May be better names for the functions and variables. Overall more readable code.
