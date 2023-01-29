"""Trie data structure for generating melody sequences

Returns:
    Trie: Trie class
"""

import random
from typing import List


class Node:
    def __init__(self):

        """
        Class representing a node in a trie data structure


        Attributes:
        frequency (int): frequency of the note stored in this node
        terminal (bool): True if the node is the end of a sequence of notes, False otherwise.
        children (dict): stores the child nodes that correspond to notes following the current note
        """
        self.frequency = 1
        self.terminal = False
        self.children = {}


class Trie:
    def __init__(self):
        self._root = Node()

    def get_root(self):
        return self._root

    def insert(self, notes: List[int]):
        """
        Insert a sequence of notes in to the trie
        Args:
            notes (List[int]): a list of notes to be inserted into the trie
        """
        current_node = self._root
        for note in notes:
            if note not in current_node.children:
                current_node.children[note] = Node()
                current_node.children[note].terminal = False
            else:
                current_node.children[note].frequency += 1
            current_node = current_node.children[note]
        current_node.terminal = True

    def get_random_note(self, current_node: Node) -> int:
        """
        Returns a child of the current node with a probability based on its frequency.

        Args:
            current_node (Node): An object of the Node class

        Returns:
            int: A random note selected based on probability
        """

        probability = {}
        total = 0
        for note in current_node.children:
            probability[note] = current_node.children[note].frequency
            total += current_node.children[note].frequency

        probability = {
            note: frequency / total for note, frequency in probability.items()
        }
        notes = list(probability.keys())
        probabilities = list(probability.values())
        return random.choices(population=notes, weights=probabilities, k=1)[0]
