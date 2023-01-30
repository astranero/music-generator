import time
import os
import pytest
import mido
from trie_module.trie import Trie


class TestTrie:
    @pytest.fixture(autouse=True)
    def initiation(self):
        pytest.trie = Trie()

    def test_insert(self):
        """
        Verifies that notes have been inserted correctly
        """
        pytest.trie.insert("A;B;C;A")
        node = pytest.trie.get_root()
        assert node.children["A"].children["B"].children["C"].children["A"].terminal
        total_freq = 0
        node = node.children["A"]
        total_freq += node.frequency
        node = node.children["B"]
        total_freq += node.frequency
        node = node.children["C"]
        total_freq += node.frequency
        total_freq += node.children["A"].frequency
        assert total_freq == 4

    def test_get_frequency(self):
        """
        Test frequencies are correct
        """
        pytest.trie.insert("A;B;C")
        pytest.trie.insert("A;D;C")
        pytest.trie.insert("A;B;C")
        assert pytest.trie.get_root().children["A"].children["B"].frequency == 2
        assert pytest.trie.get_root().children["A"].children["D"].frequency == 1

    def test_edge_case(self):
        pytest.trie.insert("A;B;A")
        assert pytest.trie.get_root().children["A"].frequency == 1

    def test_trie_get_random_note(self):
        pytest.trie.insert("A;B;C")
        note = pytest.trie.get_random_note(pytest.trie.get_root())
        assert note in "A;B;C"
