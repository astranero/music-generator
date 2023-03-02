import pytest
from markov_chain.markov import MarkovChain
from trie_module.trie import Trie


class TestMarkov:
    @pytest.fixture(autouse=True)
    def initiation(self):
        pytest.trie = Trie()

    def test_generate_melody(self):
        markov = MarkovChain(trie=pytest.trie)
        markov.insert(["A", "B", "C"], depth=3)
        melody = markov.generate_melody(prefix_notes=["A"], depth=1, melody_length=3)
        melody = "".join(melody)
        assert melody == "ABC"

    def test_second_generate_melody(self):
        """
        Test generates correct melody sequence
        """

        markov = MarkovChain(trie=pytest.trie)
        markov.insert(
            ["U", "H", "S", "F", "U", "I", "H", "S", "U", "H", "U", "H"], depth=4
        )
        melody = markov.generate_melody(
            prefix_notes=["U", "H", "S"], depth=3, melody_length=4
        )
        melody = "".join(melody)
        assert melody == "UHSF"

        melody = markov.generate_melody(
            prefix_notes=["H", "S", "F"], depth=3, melody_length=4
        )
        melody = "".join(melody)
        assert melody == "HSFU"

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
        melody = markov.generate_melody(prefix_notes=[], depth=1, melody_length=1)
        assert melody

    def test_empty_trie_generate_melody(self):
        markov = MarkovChain(trie=pytest.trie)
        markov.insert(["A"])
        melody = markov.generate_melody(prefix_notes=["A"], depth=1, melody_length=1)
        assert "A" in melody

    def test_testing_trigger(self):
        data = [
            2,
            78,
            76,
            74,
            71,
            66,
            62,
            71,
            69,
            74,
            78,
            66,
            69,
            69,
            71,
            81,
            78,
            62,
            66,
            66,
            67,
            67,
            66,
            79,
            78,
            69,
            69,
            74,
            69,
            69,
            79,
            69,
            71,
            78,
            76,
            73,
            71,
            66,
            62,
            71,
            69,
            69,
            71,
            71,
            62,
            55,
            62,
            69,
            74,
            67,
            64,
            74,
            76,
            74,
            76,
            69,
            67,
            59,
            74,
            71,
            67,
            57,
            62,
            76,
            74,
            67,
            66,
            78,
            74,
            69,
        ]
        markov = MarkovChain(trie=pytest.trie)
        markov.insert(data, depth=6)
        data_sublists = [data[x : x + 3] for x in range(0, len(data), 1)]
        melody_sublists = []

        while len(melody_sublists) < len(data_sublists):
            melody = markov.generate_melody(depth=2, melody_length=3)
            melody_sublists.append(melody)

        count = 0
        total = 0
        for data_sublist in data_sublists:
            for melody_sublist in melody_sublists:
                if melody_sublist == data_sublist:
                    count += 1
                total += 1

        percentage = count / total
        assert percentage < 0.02
