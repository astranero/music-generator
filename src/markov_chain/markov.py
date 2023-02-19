"""
Markov Chain module for generating midi file.
"""
from typing import List
from trie_module.trie import Trie


class MarkovChain:
    def __init__(self, trie: Trie = Trie()):
        self._trie = trie
        self._melody = []
        self._prefix_length = None

    def get_trie(self):
        """A Method that returns a Trie object.
        Returns:
            - Trie:
                A Trie object
        """
        return self._trie

    def insert(self, notes: List[int]):
        self._trie.insert(notes)

    def generate_melody(
        self,
        depth: int,
        melody_length: int,
        prefix_notes: List[int] = None,
    ) -> List[int]:
        """
        Generate a melody sequence based on note frequencies in the data

        Args:
            - prefix_notes (List[int]):
                prefix notes to use as the
                starting point for generating the melody
            - depth (int):
                The depth of trie.
            - melody_length (int):
                The minimum size of the returned melody str

        Returns:
            - List[int]:
                A sequence of generate notes
        """

        node = self._trie.get_root()
        if not prefix_notes:
            try:
                prefix_notes = [
                    self._trie.get_random_note(node) for i in range(depth + 1)
                ]
            except:
                print("Generation of prefix_notes wasn't possible.")
                return

        self._prefix_length = len(prefix_notes)
        self._melody = prefix_notes
        node = self._trie.search(prefix_notes)

        while len(self._melody) <= melody_length - self._prefix_length:
            current_node = node
            if not current_node.terminal:
                new_note = self._trie.get_random_note(current_node)
                if new_note:
                    self._melody.append(new_note)
                    node = current_node.children[new_note]
                else:
                    current = self._melody[-depth:]
                    node = self._trie.search(current)

            elif current_node.terminal:
                self._melody.append(current_node.note)
                current_node = self._trie.get_root()

        return self._melody
