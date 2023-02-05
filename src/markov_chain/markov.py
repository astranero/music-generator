"""
Markov Chain module for generating midi file.
"""
from typing import List
from trie_module.trie import Trie


class MarkovChain:
    def __init__(self, trie: Trie = Trie()):
        self._trie = trie
        self._melody = []
        self._prefix_lenght = None

    def get_trie(self):
        """A Method that returns a Trie object.
        Returns:
            Trie: A Trie object
        """
        return self._trie

    def insert(self, notes: List[int]):
        self._trie.insert(notes)

    def generate_melody(
        self, prefix_notes: List[int], depth: int, melody_length: int
    ) -> List[int]:
        """
        Generate a melody sequence based on note frequencies in the data

        Args:
        prefix_notes (List[int]): prefix notes to use as the
        starting point for generating the melody
        depth (int): depth of trie.
        melody_length (int): The minimum size of the returned melody str

        Returns:
        List[int]: A sequence of generate notes
        """

        node = self._trie.get_root()
        if not prefix_notes:
            prefix_notes = [self._trie.get_random_note(node) for i in range(depth)]

        self._prefix_lenght = len(prefix_notes)
        self._melody = prefix_notes

        for note in prefix_notes:
            if not node.terminal:
                node = node.children[note]

        while len(self._melody) <= melody_length - self._prefix_lenght:
            current_node = node
            current = self._melody[-depth:]
            for note in current:
                if note in current_node.children:
                    current_node = current_node.children[note]
                else:
                    current_node = self._trie.get_root()

            new_note = self._trie.get_random_note(current_node)
            self._melody.append(new_note)
            node = current_node.children[new_note]
        return self._melody
