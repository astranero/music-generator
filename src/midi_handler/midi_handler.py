import os
import random
import sys

from mido import Message, MidiFile, MidiTrack
from midi2audio import FluidSynth
from pygame import mixer

sys.path.append(os.fsdecode(os.getcwd() + "/src/"))
from markov_chain.markov import MarkovChain


class MidiHandler:
    def __init__(self):
        self._directory = os.fsdecode(os.getcwd() + "/Data/")
        self._file_synth = FluidSynth(
            sound_font=(os.fsdecode(os.getcwd() + "/undertale.sf2"))
        )
        self._mav_file_path = os.fsdecode(os.getcwd() + "/generated.wav")
        self._mid = None
        self._music = None
        self.markov = MarkovChain()
        self._initiate_mixer()

    def _initiate_mixer(self):
        mixer.init()
        mixer.music.set_volume(0.5)
        self._music = mixer.music

    def initiate_markov(self):
        print("Reading data to Trie data structure")
        filenames = [
            f for f in os.listdir(self._directory) if f.endswith((".MID", ".mid"))
        ]

        filenames = [
            f for f in os.listdir(self._directory) if f.endswith((".MID", ".mid"))
        ]
        mid_files = []
        for filename in filenames:
            try:
                mid_files.append(MidiFile((self._directory + filename)))
            except (EOFError, ValueError, IOError):
                pass
        mid_tracks = [t for mid in mid_files for i, t in enumerate(mid.tracks)]

        for i, track in enumerate(mid_tracks):
            notes = []
            count = 0
            for msg in track:
                if msg.type == "note_on":
                    notes.append(msg.note)
                if count == 8:
                    count = 0
                    self.markov.insert(notes)
                    notes = []
                count += 1

        print("Initiation of Trie data structure is done.")

    def generate_midi(self):

        print("Generating melody...")

        notes = []
        while len(notes) < 500:
            melody = self.markov.generate_melody()
            notes = notes + melody

        print("Melody generation done.")

        midf = MidiFile()
        track = MidiTrack()
        midf.tracks.append(track)
        tick_time = 0
        for note in notes:
            track.append(
                Message(
                    "note_on",
                    note=note,
                    velocity=random.randint(90, 120),
                    time=tick_time,
                )
            )
            tick_time += 5

        midf.save(self._directory + "generated.mid")
        self.generate_mav(self._directory + "generated.mid")

    def read_mid_file(self, filename):
        self._mid = MidiFile(self._directory + filename, clip=True)

    def play_music(self):
        mixer.music.load(self._mav_file_path)
        self._music.play()
        return self._music

    def pause_music(self):
        self._music.pause()

    def resume_music(self):
        self._music.unpause()

    def stop_music(self):
        self._music.stop()

    def generate_mav(self, file_path):
        self._file_synth.midi_to_audio(file_path, "generated.wav")


if __name__ == "__main__":
    handler = MidiHandler()
    handler.initiate_markov()
    handler.generate_midi()
    handler.play_music()
