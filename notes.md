Create a TrieNode class that contains the following properties:

A dictionary that stores the next possible notes for the current note, along with their frequency.
A boolean value indicating whether the current node represents the end of a note sequence.
Create a Trie class that contains the following methods:

A build method that takes in a dataset of existing music and constructs the Trie by adding each note sequence to the Trie.
A add_sequence method that takes in a sequence of notes and adds it to the Trie by traversing the Trie and updating the frequency of each note in the sequence.
A get_next_notes method that takes in a note and returns the next possible notes along with their frequencies.
Create a MarkovChain class that contains the following methods:

A build method that takes in the Trie and a sequence length, and constructs the Markov Chain by analyzing the patterns in the Trie.
A generate_sequence method that takes in a starting note and generates a new sequence of notes using the probabilities stored in the Markov Chain.
In the main function, first, use the Trie class to build the Trie from the dataset of existing music.

Next, use the MarkovChain class to build the Markov Chain from the Trie and the desired sequence length.
Finally, use the MarkovChain class to generate a new sequence of notes by providing a starting note and the desired length of the sequence.
You can experiment with different sequence lengths and starting notes to generate different variations of music.

Set a neighbor => Note node with frequencies and neighbors
Converting message to bytes with mido, and inserting it to the Trie.. Test if it produces anything funny.
