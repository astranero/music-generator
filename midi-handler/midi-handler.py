from mido import Message, MidiFile
import os
import time
from midi2audio import FluidSynth
from pygame import mixer


class MidiHandle:
    def __init__(self):
        self._directory = os.fsdecode(os.getcwd() + "/Data/")
        self._file_synth = FluidSynth()
        self._mav_file_path = os.fsdecode(os.getcwd() + "/generated.wav")
        self._mid = None
        self._mixer = mixer
        self._mixer.init()
        self._music = self._mixer.music
        self._music.load(self._mav_file_path)
        self._music.set_volume(0.5)

    def read_mid_file(self, filename):
        self._mid = MidiFile(self._directory + filename, clip=True)

    def print_messages(self):
        for i, track in enumerate(self._mid.tracks):
            for msg in track:
                print(msg)

    def play_music(self):
        self._music.play()
        return self._music

    def pause_music(self):
        self._music.pause()

    def resume_music(self):
        self._music.unpause()

    def stop_music(self):
        self._music.stop()

    def generate_mav(self, filename):
        self._file_synth.midi_to_audio(self._directory + filename, "generated.wav")


if __name__ == "__main__":
    handler = MidiHandle()
    music = handler.play_music()
    while music.get_busy():
        time.sleep(10)
    handler.pause_music()
    while handler.
