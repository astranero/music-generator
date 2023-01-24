from mido import Message, MidiFile
import os
from midi2audio import FluidSynth


class MidiHandle:
    def __init__(self):
        self._directory = os.fsdecode(os.getcwd() + "/Data/")
        self._file_synth = FluidSynth()
        self._mid = None

    def read_mid_file(self, filename):
        self._mid = MidiFile(self._directory + filename, clip=True)

    def print_messages(self):
        for i, track in enumerate(self._mid.tracks):
            for msg in track:
                print(msg)

    def play_midi(self, filename):
        self._file_synth.play_midi(self._directory + filename)

    def generate_mav(self, filename):
        self._file_synth.midi_to_audio(self._directory + filename, "generated.wav")


if __name__ == "__main__":
    handler = MidiHandle()
    handler.read_mid_file("3x3 Eyes (1992) - MUS_36.MID")
    handler.play_midi("3x3 Eyes (1992) - MUS_36.MID")
    handler.print_messages()
