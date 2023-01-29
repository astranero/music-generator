"""
Markov Chain module for generating midi file.
"""

from trie_ds.trie import Trie


class MarkovChain:
    def __init__(self, trie: Trie = Trie()):
        self.trie = trie
