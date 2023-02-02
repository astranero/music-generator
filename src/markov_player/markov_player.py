import os
import random
import sys
from typing import List

from mido import Message, MidiFile, MidiTrack, MetaMessage
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

    def _get_midi_files(self, filenames: List[str]) -> List[MidiFile]:
        """A method to generate MidiFile objects from midi files.

        Args:
            filenames (List[str]): A list of midi filenames.

        Returns:
            List[MidiFile]: A list of MidiFile objects.
        """
        midifiles = []
        for filename in filenames:
            try:
                midifiles.append(MidiFile((self._data_directory + filename)))
            except Exception:
                pass
        return midifiles

    def _get_tracks(self, midifiles: List[MidiFile]) -> List[MidiTrack]:
        """A method to parse MidiTrack objects from a list of MidiFiles.

        Args:
            mid_files (List[MidiFile]): A list of MidiFile objects.

        Returns:
            List[MidiTrack]: A list of MidiTrack objects.
        """
        mid_tracks = [track for mid in midifiles for track in mid.tracks]
        return mid_tracks

    def _track_messages_to_notes(self, tracks: List[MidiTrack]) -> List[int]:
        for i, track in enumerate(tracks):
            notes = []
            for msg in track:
                if msg.type == "note_on":
                    notes.append(msg.note)
            yield notes

    def _notes_depth_size_sublist(
        self, tracks: List[MidiTrack], depth: int
    ) -> List[List[int]]:

        for notes in self._track_messages_to_notes(tracks):
            for i in range(len(notes) - depth + 1):
                yield notes[i : i + depth]

    def _insert_into_trie(self, tracks: List[MidiTrack], depth: int) -> None:
        """A method that inserts string notes of lenght 2 to 12 i from MidiTrack objects
        into Markov Chains Trie data structure.

        Args:
            tracks (List[MidiTrack]): A list of MidiTrack objects.
        """

        for sequence in self._notes_depth_size_sublist(tracks, depth=depth):
            self._markov.insert(sequence)

    def _generate_notes(
        self,
        prefix_notes: List[int],
        depth: int,
        melody_lenght: int,
    ) -> List[int]:
        """A method that generates a list of notes.

        Returns:
            List[str]: A list of string type notes.
        """
        print("Generating melody...")
        notes = self._markov.generate_melody(
            prefix_notes=prefix_notes, depth=depth, melody_lenght=melody_lenght
        )
        print("Melody generation is complete.")
        return notes

    def _create_midifile(
        self,
        prefix_notes: List[int],
        depth: int,
        melody_lenght: int,
    ) -> MidiFile:
        """A method that creates a midifile using a Markov Chain.

        Returns:
            MidiFile: A MidiFile object.
        """
        notes = self._generate_notes(
            prefix_notes=prefix_notes, depth=depth, melody_lenght=melody_lenght
        )

        midifile = MidiFile(type=2)
        track = MidiTrack()
        midifile.tracks.append(track)
        time_tick = 0
        velocity = 0
        channel = 4

        for i, note in enumerate(notes):
            if i < len(notes) - 10:
                time_tick += 2
                track.append(
                    self._note(
                        note=note,
                        velocity=velocity,
                        time_tick=time_tick,
                        channel=channel,
                    )
                )

                velocity += random.randint(1, 2)
                if velocity > 127:
                    velocity = random.randint(98, 104)
                elif velocity < 0:
                    velocity = 0
            else:
                time_tick += random.randint(1, 2)
                track.append(
                    self._note(
                        note=note,
                        velocity=velocity,
                        time_tick=time_tick,
                        channel=channel,
                    )
                )
                velocity -= 5

        return midifile

    def _note(
        self,
        time_tick,
        note: int,
        velocity: int,
        channel: int,
    ):
        return Message(
            "note_on",
            channel=channel,
            note=int(note),
            velocity=velocity,
            time=time_tick,
        )

    def initiate_markov(self, depth: int = 1):
        print("Setting up Markov Chain: Loading filenames...")
        filenames = self._get_filenames()
        print(" > Filenames loaded: Generating midi files...")
        midifiles = self._get_midi_files(filenames)
        print(" > Generation of midfiles complete: Setting up tracks...")
        tracks = self._get_tracks(midifiles)
        print(" > Inserting data to Trie Data Structure.")
        self._insert_into_trie(tracks, depth=depth)
        print(" > Initiation of Trie Data Structure is done.")
        print("Setting up Markov Chain is complete.")

    def generate_music(
        self,
        filename: str,
        prefix_notes: List[int] = None,
        depth: int = 4,
        melody_lenght: int = 250,
    ):
        self._set_filenames(filename)
        print("Generation of new midifile.")
        midifile = self._create_midifile(
            prefix_notes=prefix_notes, depth=depth, melody_lenght=melody_lenght
        )
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
    player.play_music("Rockin")
