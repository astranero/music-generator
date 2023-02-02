"""Trie data structure for generating melody sequences

Returns:
    Trie: Trie class
"""

import random
from typing import List


class Node:
    def __init__(self, note: str):

        """
        Class representing a node in a trie data structure


        Attributes:
        frequency (int): frequency of the note stored in this node
        terminal (bool): True if the node is the end of a sequence of notes, False otherwise.
        children (dict): stores the child nodes that correspond to notes following the current note
        """
        self.note = note
        self.frequency = 0
        self.terminal = False
        self.children = {}


class Trie:
    def __init__(self):
        self._root = Node(None)

    def get_root(self):
        return self._root

    def insert(self, notes: List[int]):
        """
        Insert a sequence of notes in to the trie
        Args:
            notes (List[int]): a list of notes to be inserted into the trie
        """

        node = self._root
        for note in notes:
            if note not in node.children:
                node.children[note] = Node(note)
            node.children[note].frequency += 1
            node = node.children[note]
        node.terminal = True

    def get_random_note(self, node: Node) -> str:
        """
        Returns a child of the current node with a probability based on its frequency.

        Args:
            node (Node): An object of the Node class

        Returns:
            str: A random note selected based on probability
        """

        probability = {}
        total = 0
        for note in node.children:
            probability[note] = node.children[note].frequency
            total += node.children[note].frequency
        probability = {
            note: frequency / total for note, frequency in probability.items()
        }
        notes = list(probability.keys())
        probabilities = list(probability.values())
        return random.choices(population=notes, weights=probabilities, k=1)[0]
