"""
Markov Chain module for generating midi file.
"""
from typing import List
from trie_module.trie import Trie


class MarkovChain:
    def __init__(self, trie: Trie = Trie()):
        self._trie = trie
        self._prefix_length = None

    def get_trie(self):
        """A Method that returns a Trie object.
        Returns:
            - Trie:
                A Trie object
        """
        return self._trie

    def _notes_depth_size_sublist(
        self, notes: List[int], depth: int
    ) -> List[List[int]]:
        """A method to split notes in the track into smaller depth sized sublists.
        Args:
            notes (List[int]): Notes from the track
            depth (int): The size of the sublists

        Yields:
            Iterator[List[List[int]]]: A sublist of sized depth that contain notes
        """
        for i in range(len(notes) - depth + 1):
            yield notes[i : i + depth]

    def insert(self, notes: List[int], depth: int = 2):
        """A method to insert notes of depth sized sublists into Trie.
        Args:
            notes (List[int]): The notes from the track
            depth (int, optional): The order of the trie. Defaults to 2.
        """
        for sequence in self._notes_depth_size_sublist(notes, depth=depth):
            self._trie.insert(sequence)

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
                A sequence of generated notes
        """
        melody = []
        if not prefix_notes:
            prefix_notes = []

        melody = prefix_notes
        current_node = self._trie.search(self._trie.get_root(), prefix_notes)

        while len(melody) < melody_length:
            if current_node.terminal:
                melody.append(current_node.note)
                current_node = self._trie.get_root()

            new_note = self._trie.get_random_note(current_node)
            melody.append(new_note)
            last_notes = melody[-depth:]
            current_node = self._trie.search(current_node, last_notes)
        return melody
