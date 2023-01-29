import time
import pytest
from trie_ds.trie import Trie


class TestTrie:
    @pytest.fixture(autouse=True)
    def initiation(self):
        pytest.trie = Trie()

    def test_insert(self):
        """
        Verifies that notes have been inserted correctly
        """
        pytest.trie.insert(["A", "B", "C"])
        node = pytest.trie.get_root()
        assert node.children["A"].children["B"].children["C"].terminal
        total_freq = 0
        node = node.children["A"]
        total_freq += node.frequency
        node = node.children["B"]
        total_freq += node.frequency
        node = node.children["C"]
        total_freq += node.frequency
        assert total_freq == 3

    def test_generate_melody(self):
        pytest.trie.insert(["A", "B", "C"])
        melody = pytest.trie.generate_melody("A")
        assert melody == ["B", "C"]

    def test_second_generate_melody(self):
        trie = pytest.trie
        trie.insert(["A", "B", "C"])
        trie.insert(["A", "B", "D"])
        trie.insert(["A", "B", "E"])
        melody = trie.generate_melody(["A", "B"])
        assert melody in [["C"], ["D"], ["E"]]

    def test_get_frequency(self):
        trie = pytest.trie
        trie.insert(["A", "B", "C"])
        trie.insert(["A", "D", "C"])
        trie.insert(["A", "B", "C"])
        assert trie.get_root().children["A"].children["B"].frequency == 2
        assert trie.get_root().children["A"].children["D"].frequency == 1

    def test_edge_case(self):
        trie = pytest.trie
        trie.insert(["A", "B", "A"])
        assert trie.get_root().children["A"].frequency == 1

    def test_large_data_set(self):
        start_time = time.time()
        elapsed_time = time.time() - start_time
