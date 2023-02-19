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
            71,
            74,
            78,
            66,
            69,
            71,
            69,
            78,
            81,
            74,
            81,
            78,
            81,
            66,
            62,
            62,
            71,
            62,
            62,
            74,
            78,
            76,
            81,
            69,
            69,
            78,
            76,
            62,
            64,
            76,
            78,
            76,
            74,
            67,
            66,
            64,
            60,
            74,
            74,
            81,
            79,
            62,
            64,
            62,
            66,
            79,
            78,
            74,
            73,
            62,
            66,
            78,
            76,
            74,
            78,
            66,
            64,
            69,
            81,
            78,
            74,
            73,
            74,
            74,
            79,
            76,
            74,
            64,
            62,
            81,
            78,
            79,
            78,
            62,
            62,
            76,
            76,
            66,
            64,
            69,
            66,
            76,
            76,
            73,
            76,
            78,
            79,
            81,
            81,
            79,
            81,
            69,
            66,
            71,
            69,
            74,
            81,
            69,
            71,
            55,
            59,
            78,
            74,
            66,
            62,
            69,
            69,
            81,
            78,
            76,
            74,
            66,
            69,
            81,
            69,
            74,
            78,
            69,
            74,
            76,
            76,
            66,
            69,
            69,
            69,
            73,
            74,
            74,
            76,
            69,
            71,
            76,
            74,
            73,
            74,
            66,
            62,
            69,
            71,
            78,
            79,
            66,
            67,
            76,
            76,
            71,
            67,
            62,
            69,
            66,
            67,
            67,
            71,
            78,
            79,
            62,
            62,
            66,
            67,
            74,
            76,
            62,
            69,
            74,
            69,
            71,
            73,
            66,
            62,
            76,
            81,
            69,
            69,
            79,
            76,
            78,
            79,
            62,
            69,
            81,
        ]
        markov = MarkovChain(trie=pytest.trie)
        markov.insert(data)
        data_sublists = [data[x : x + 3] for x in range(0, len(data), 1)]
        melody_sublists = []

        while melody_sublists < data_sublists:
            melody_sublists.append(markov.generate_melody(depth=2, melody_length=100))

        count = 0
        total = 0
        for data_sublist in data_sublists:
            for melody_sublist in melody_sublists:
                if melody_sublist == data_sublist:
                    count += 1
                print(melody_sublist, data_sublist)
                total += 1

        percentage = count / len(data_sublists)
        assert percentage > 0.001
