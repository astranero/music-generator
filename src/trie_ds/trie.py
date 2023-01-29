"""Trie data structure for generating melody sequences

Returns:
    Trie: returns Trie class
"""

import random
from typing import List


class Node:
    def __init__(self):
        """This is trie node that stores note, and its childrens that come after it.

        Args:
            note (str): note of a midi file. Defaults to None.
        Vars:
            terminal (bool): True, if node is end of trie and doesn't contain note value,
            otherwise False.
            children (dict): stores notes that follow current note.
            frequency (int): frequency of note.
        """
        self.frequency = 1
        self.terminal = False
        self.children = {}


class Trie:
    def __init__(self):
        self._root = Node()
        self._root.terminal = True

    def get_root(self):
        return self._root

    def generate_melody(self, prefix_note) -> List[str]:
        current_node = self._root
        ret_notes = []

        for note in prefix_note:
            if note not in current_node.children:
                return "Note not found"
            current_node = current_node.children[note]

        while not current_node.terminal:
            new_note = self._get_random_note(current_node)
            ret_notes.append(new_note)
            current_node = current_node.children[new_note]

        return ret_notes

    def insert(self, notes: List[str]) -> bool:
        current_node = self._root
        for note in notes:
            if note not in current_node.children:
                current_node.children[note] = Node()
            else:
                current_node.children[note].frequency += 1
            current_node = current_node.children[note]
        current_node.terminal = True

    def _get_random_note(self, current_node):
        probability = {}
        total = 0
        for note in current_node.children:
            probability[note] = current_node.children[note].frequency
            total += current_node.children[note].frequency

        probability = {k: v / total for k, v in probability.items()}
        notes = list(probability.keys())
        probabilities = list(probability.values())
        return random.choices(population=notes, weights=probabilities, k=1)[0]
