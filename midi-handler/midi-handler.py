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
        self._music = None
        self._initiate_mixer()

    def _initiate_mixer(self):
        mixer.init()
        mixer.music.set_volume(0.5)
        self._music = mixer.music

    def read_mid_file(self, filename):
        self._mid = MidiFile(self._directory + filename, clip=True)

    def print_messages(self):
        for i, track in enumerate(self._mid.tracks):
            for msg in track:
                print(msg)

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

    def generate_mav(self, filename):
        self._file_synth.midi_to_audio(self._directory + filename, "generated.wav")


if __name__ == "__main__":
    handler = MidiHandle()
    handler.generate_mav("1943 - Assault On Surface Forces B.MID")
    music = handler.play_music()
    handler.read_mid_file("1943 - Assault On Surface Forces B.MID")
    handler.print_messages()
    while music.get_busy():
        time.sleep(10)
        handler.pause_music()
    time.sleep(5)
    handler.resume_music()
    while music.get_busy():
        time.sleep(5)
