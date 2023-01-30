"""
Markov Chain module for generating midi file.
"""

from trie_module.trie import Trie


class MarkovChain:
    def __init__(self, trie: Trie = Trie()):
        self._trie = trie
        self._melody = ""

    def get_trie(self):
        """A Method that returns a Trie object.
        Returns:
            Trie: A Trie object
        """
        return self._trie

    def insert(self, notes: str):
        self._trie.insert(notes)

    def generate_melody(self, prefix_notes: str = None, lenght: int = 500) -> str:
        """
        Generate a melody sequence based on note frequencies in the data

        Args:
        prefix_notes (str): prefix notes to use as the
        starting point for generating the melody
        lenght (int): The minimum size of the returned melody str

        Returns:
        str: generated melody as a string of notes
        """

        node = self._trie.get_root()
        if not prefix_notes:
            prefix_notes = self._trie.get_random_note(node)

        for note in prefix_notes:
            if note not in node.children:
                node = self._trie.get_root()
            else:
                node = node.children[note]

        while lenght > len(self._melody):
            while not node.terminal:
                new_note = self._trie.get_random_note(node)
                self._melody += new_note
                self._melody += ";"
                node = node.children[new_note]
            node = self._trie.get_root()

        return self._melody
