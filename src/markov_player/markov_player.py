import os
import random
import sys
import time
from typing import List

from mido import Message, MidiFile, MidiTrack
from midi2audio import FluidSynth
from pygame import mixer
from dotenv import dotenv_values

sys.path.append(os.fsdecode(os.getcwd() + "/src/"))
from markov_chain.markov import MarkovChain

env_values = dotenv_values(".env")


class MarkovPlayer:
    """
    A class that generates and controls music using A Markov Chain.
    """

    def __init__(self, markov: MarkovChain = MarkovChain()):
        self._data_directory = os.fsdecode(os.getcwd() + env_values["DATA_PATH"])
        self._file_synth = FluidSynth(
            sound_font=(os.fsdecode(os.getcwd() + env_values["SOUNDFONT"]))
        )
        self._file_path = os.fsdecode(os.getcwd()) + "/"
        self._music = None
        self._markov = markov
        self._filename_mid = None
        self._filename_wav = None
        self._initiate_mixer()

    def _initiate_mixer(self):
        mixer.init()
        mixer.music.set_volume(0.5)
        self._music = mixer.music

    def _get_filenames(self) -> List[str]:
        """A method to fetch midi filenames.

        Returns:
            List[str]: A list of filenames.
        """

        filenames = [
            filename
            for filename in os.listdir(self._data_directory)
            if filename.endswith((".MID", ".mid"))
        ]
        return filenames

    def _get_mid_files(self, filenames: List[str]) -> List[MidiFile]:
        """A method to generate MidiFile objects from midi files.

        Args:
            filenames (List[str]): A list of midi filenames.

        Returns:
            List[MidiFile]: A list of MidiFile objects.
        """
        mid_files = []
        for filename in filenames:
            try:
                mid_files.append(MidiFile((self._data_directory + filename)))
            except Exception:
                pass
        return mid_files

    def _get_tracks(self, mid_files: List[MidiFile]) -> List[MidiTrack]:
        """A method to parse MidiTrack objects from a list of MidiFiles.

        Args:
            mid_files (List[MidiFile]): A list of MidiFile objects.

        Returns:
            List[MidiTrack]: A list of MidiTrack objects.
        """
        mid_tracks = [track for mid in mid_files for track in mid.tracks]
        return mid_tracks

    def _insert_into_trie(self, tracks: List[MidiTrack]) -> None:
        """A method that inserts string notes of lenght 2 to 12 i from MidiTrack objects
        into Markov Chains Trie data structure.

        Args:
            tracks (List[MidiTrack]): A list of MidiTrack objects.
        """
        for i, track in enumerate(tracks):
            notes = ""
            count = 0
            for msg in track:
                if msg.type == "note_on":
                    notes += str(msg.note)
                    notes += ";"
                if count == random.randint(2, 12):
                    count = 0
                    self._markov.insert(notes)
                    notes = ""
                count += 1

    def _generate_notes(self) -> List[str]:
        """A method that generates a list of notes.

        Returns:
            List[str]: A list of string type notes.
        """
        print("Generating melody...")
        melody = self._markov.generate_melody(lenght=2000)
        print("Melody generation is complete.")
        notes = [note for note in list(filter(None, melody.split(";")))]
        return notes

    def _create_midifile(self) -> MidiFile:
        """A method that creates a midifile using a Markov Chain.

        Returns:
            MidiFile: A MidiFile object.
        """
        notes = self._generate_notes()
        midifile = MidiFile()
        track = MidiTrack()
        midifile.tracks.append(track)
        time_tick = 0
        count = 0
        volume = 100

        for note in notes:
            track.append(Message("note_on", note=note, velocity=volume, time=time_tick))

            if count == random.randint(1, 2):
                time_tick += random.randint(0, 2)
                count = 0
            else:
                time_tick += 1

            volume += random.randint(4, 5)
            count += 1

            if volume > 127:
                volume = 127

            elif volume < 0:
                volume = 0

        return midifile

    def initiate_markov(self):
        print("Setting up Markov Chain: Loading filenames...")
        filenames = self._get_filenames()
        print(" > Filenames loaded: Generating midfiles...")
        mid_files = self._get_mid_files(filenames)
        print(" > Generation of midfiles complete: Setting up tracks...")
        tracks = self._get_tracks(mid_files)
        print(" > Inserting data to Trie Data Structure.")
        self._insert_into_trie(tracks)
        print(" > Initiation of Trie Data Structure is done.")
        print("Setting up Markov Chain is complete.")

    def generate_music(self, filename: str):
        self._set_filenames(filename)
        print("Generation of new midifile.")
        midifile = self._create_midifile()
        print(" > Saving midifile...")
        self._save_midifile(midifile)
        print(" > Generating wav file...")
        self._generate_mav()
        print("Music generation complete.")

    def _save_midifile(self, midifile: MidiFile):
        midifile.save(self._file_path + self._filename_mid)

    def play_music(self, filename: str):
        mixer.music.load(self._file_path + filename + ".wav")
        self._music.play()
        return self._music

    def pause_music(self):
        self._music.pause()

    def resume_music(self):
        self._music.unpause()

    def stop_music(self):
        self._music.stop()

    def _set_filenames(self, filename: str):
        self._filename_mid = filename + ".mid"
        self._filename_wav = filename + ".wav"

    def _generate_mav(self):
        self._file_synth.midi_to_audio(
            self._file_path + self._filename_mid, self._filename_wav
        )


if __name__ == "__main__":
    player = MarkovPlayer()
    player.initiate_markov()
    player.generate_music("Rockin")
    while player.play_music("Rockin"):
        time.sleep(25)
