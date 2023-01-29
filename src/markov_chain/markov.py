"""
Markov Chain module for generating midi file.
"""
from typing import List
from trie_module.trie import Trie


class MarkovChain:
    def __init__(self, trie: Trie = Trie()):
        self._trie = trie

    def get_trie(self):
        return self._trie

    def insert(self, notes: List[int]):
        self._trie.insert(notes)

    def generate_melody(self, prefix_notes: List[int] = None) -> List[int]:
        """
        Generate a melody sequence based on note frequencies in the data

        Args:
        prefix_notes (List[int]): prefix notes to use as the
        starting point for generating the melody
        minimum_size (int): The minimum size of the returned melody list

        Returns:
        List[int]: generated melody as a list of notes
        """

        current_node = self._trie.get_root()
        ret_notes = []
        if not prefix_notes:
            prefix_notes = [self._trie.get_random_note(current_node)]

        for note in prefix_notes:
            if note not in current_node.children:
                return []
            else:
                current_node = current_node.children[note]

        while not current_node.terminal:
            new_note = self._trie.get_random_note(current_node)
            ret_notes.append(new_note)
            current_node = current_node.children[new_note]
        return ret_notes
