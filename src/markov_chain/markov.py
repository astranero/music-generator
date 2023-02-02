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
        self,
        prefix_notes: List[int],
        depth: int,
        melody_lenght: int,
        initiation: bool = True,
    ) -> List[int]:
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
            prefix_notes = []
            while len(prefix_notes) < depth:
                prefix_notes.append(self._trie.get_random_note(node))

        if initiation:
            self._prefix_lenght = len(prefix_notes)
            self._melody += prefix_notes

        for note in prefix_notes:
            if note in node.children:
                node = node.children[note]
            else:
                node = self._trie.get_root()

        while not node.terminal:
            new_note = self._trie.get_random_note(node)
            self._melody.append(new_note)
            node = node.children[new_note]

        while len(self._melody) <= melody_lenght - self._prefix_lenght:
            current = self._melody[
                len(self._melody) - depth - 1 : len(self._melody) - 1
            ]
            self._melody = self.generate_melody(
                prefix_notes=current,
                depth=depth,
                melody_lenght=melody_lenght,
                initiation=False,
            )
        return self._melody
