import time
import os
import pytest
import mido
from markov_chain.markov import MarkovChain
from trie_module.trie import Trie


class TestMarkov:
    @pytest.fixture(autouse=True)
    def initiation(self):
        pytest.trie = Trie()

    def test_generate_melody(self):
        markov = MarkovChain(trie=pytest.trie)
        markov.insert("A;B;C")
        melody = markov.generate_melody(prefix_notes="A")
        assert len(melody) >= 2

    def test_second_generate_melody(self):
        """
        Test generates correct melody sequence
        """
        markov = MarkovChain(trie=pytest.trie)
        markov.insert("A;B;C;B")
        markov.insert("A;B;D;C")
        markov.insert("A;A;F;E")

        melody = markov.generate_melody(prefix_notes="A")
        assert len(melody) >= 2

    def test_nonexisting_note_generate_melody(self):
        """
        Test if given note doesn't exist then randomly
        choose prefix note from children notes.
        """
        markov = MarkovChain(trie=pytest.trie)
        markov.insert("A;B;C")
        markov.insert("A;C;D")
        markov.insert("C;B;C;E")
        melody = markov.generate_melody(prefix_notes="A;B")
        assert melody

    def test_empty_list_generate_melody(self):
        markov = MarkovChain(trie=pytest.trie)
        markov.insert("A;B;C")
        markov.insert("A;C;D")
        markov.insert("C;B;C;E")
        melody = markov.generate_melody()
        assert melody

    def test_empty_trie_generate_melody(self):
        markov = MarkovChain(trie=pytest.trie)
        markov.insert("A")
        melody = markov.generate_melody()
        assert melody not in []

    def test_large_data_set(self):
        """Test that trie works in resonable amount of time"""
        start_time = time.time()
        directory = os.fsdecode(os.getcwd() + "/Data/")
        markov = MarkovChain(trie=pytest.trie)
        filenames = [f for f in os.listdir(directory) if f.endswith((".MID", ".mid"))]
        mid_files = []
        for filename in filenames:
            try:
                mid_files.append(mido.MidiFile((directory + filename)))
            except Exception:
                pass
        mid_tracks = [t for mid in mid_files for i, t in enumerate(mid.tracks)]

        for i, track in enumerate(mid_tracks):
            notes = ""
            count = 0
            for msg in track:
                if msg.type == "note_on":
                    notes += str(msg.note)
                if count == 8:
                    count = 0
                    markov.insert(notes)
                    notes = ""
                count += 1

        notes = ""
        melody = markov.generate_melody()
        notes += melody + ";"
        assert notes
        elapsed_time = time.time() - start_time
        assert elapsed_time < 120
