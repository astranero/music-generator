import pytest
from markov_chain.markov import MarkovChain
from trie_module.trie import Trie


class TestMarkov:
    @pytest.fixture(autouse=True)
    def initiation(self):
        pytest.trie = Trie()

    def test_generate_melody(self):
        markov = MarkovChain(trie=pytest.trie)
        markov.insert(["A", "B", "C"])
        melody = markov.generate_melody(prefix_notes=["A"], depth=1, melody_length=3)
        melody = "".join(melody)
        assert melody == "ABC"

    def test_second_generate_melody(self):
        """
        Test generates correct melody sequence
        """
        markov = MarkovChain(trie=pytest.trie)
        markov.insert(["A", "B", "C", "B"])
        markov.insert(["A", "B", "D", "C"])
        markov.insert(["A", "A", "F", "E"])

        melody = markov.generate_melody(
            prefix_notes=["A", "B"], depth=3, melody_length=4
        )
        melody = "".join(melody)
        assert (melody == "ABC") or (melody == "ABD")

    def test_nonexisting_note_generate_melody(self):
        """
        Test if given note doesn't exist then randomly
        choose prefix note from children notes.
        """
        markov = MarkovChain(trie=pytest.trie)
        markov.insert(["A", "B", "C"])
        markov.insert(["A", "C", "D"])
        markov.insert(["C", "B", "C", "E"])
        melody = markov.generate_melody(
            prefix_notes=["A", "B", "G"], depth=3, melody_length=3
        )
        assert melody

    def test_empty_list_generate_melody(self):
        markov = MarkovChain(trie=pytest.trie)
        markov.insert(["A", "B", "C"])
        markov.insert(["A", "C", "D"])
        markov.insert(["C", "B", "C", "E"])
        melody = markov.generate_melody(prefix_notes=[], depth=0, melody_length=0)
        assert melody

    def test_empty_trie_generate_melody(self):
        markov = MarkovChain(trie=pytest.trie)
        markov.insert(["A"])
        melody = markov.generate_melody(prefix_notes=["A"], depth=1, melody_length=1)
        assert "A" in melody
    
    def test_testing_trigger(self):
        assert True == True
