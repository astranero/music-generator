import re
import random
import time
from art import tprint
from markov_player.markov_player import MarkovPlayer


class UserInterface:
    def __init__(self, player: MarkovPlayer = MarkovPlayer()):
        self._player = player
        self._filename = None
        self._trie_initiated = False

        self._start_controller = {
            "i": self._initiate_markov,
            "s": self._play_menu,
            "g": self._generate_music,
        }
        self._start_menu()

    def _start_menu(self):
        print(
            "__________________________________________________________________________________________________________________________"
        )
        tprint("Music Generator")
        self._print_picture()
        print(self._start_commands())
        while True:

            key = str(input("Command: "))
            if key == "e":
                break
            try:
                func = self._start_controller[key]
                func()
            except KeyError:
                print("Incorrect command!")

    def _play_menu(self):
        playing = True
        if self._filename:
            self._player.load_music(self._filename)
            self._player.play_music()
            while True:
                self._print_picture()
                print(self._play_commands())
                key = input("Command: ")
                if key == "p":
                    if playing:
                        self._player.pause_music()
                        playing = False
                    else:
                        self._player.resume_music()
                        playing = True
                elif key == "x":
                    self._player.stop_music()
                    break
        else:
            print("FileNotFound: Please generate a music file.")

    def _start_commands(self) -> str:
        return """
> i to initiate music player with data files.
> g to generate a new music file.
> s to start the music!
> e to exit.
__________________________________________________________________________________________________________________________
"""

    def _play_commands(self) -> str:
        return """
> p to pause/unpause. 
> x to exit back to main menu.
__________________________________________________________________________________________________________________________
"""

    def _print_picture(self) -> print:
        return print(
            self._sexy_woman(),
        )

    def _initiate_markov(self):
        try:
            depth = (
                input(
                    "Please select a depth for the trie data structure (Optional, Defaults to 2): "
                )
                or 2
            )
            depth = int(depth)
        except ValueError:
            print("Value must be integer. Please try again.")

        try:
            self._player.initiate_markov(depth)
        except FileNotFoundError:
            print("FileNotFoundError: Data files not found.")
            print("Please insert Data Files to the Data folder, and try again.")

    def _generate_music(self):
        try:
            filename = str(input("Insert a name for the music file: "))
            prefix_notes = (
                str(input("Insert prefix notes in format; '2;121;22;11' (Optional): "))
                or None
            )

            depth = (
                input(
                    "Insert the depth of the data to be used for generation (Optional, Defaults to 2): "
                )
                or 2
            )
            depth = int(depth)
            self._filename = filename

        except ValueError as exc:
            print(f"{exc}")

        if self._prefix_validation(prefix_notes):
            try:
                self._player.generate_music(
                    filename=filename, prefix_notes=prefix_notes, depth=depth
                )
            except RecursionError:
                print("GenerationError: Please iniatiate music player with data files.")
        else:
            print(
                "Prefix notes must be a sequence of integers between 1 and 127, separated by semicolons."
            )
            print("Example: '1;123;104;67;22'")

    def _prefix_validation(self, prefix_notes: str) -> bool:
        if prefix_notes:
            regex = r"^(?:(?:[1-9]|[1-9][0-9]|1[0-1][0-9]|12[0-7]);)*(?:[1-9]|[1-9][0-9]|1[0-1][0-9]|12[0-7])$"
            return re.match(regex, prefix_notes) is not None
        return True

    def _sexy_woman(self):
        return """ 
    
                        ⢀⣤⣴⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⡿⠛⢻⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⠇⢀⣸⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⡟⠉⠀⠀⠀⢻⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠿⠣⡀⠀⠒⣶⣿⣿⣿⡏⢿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠏⠀⠀⠀⢸⣶⣶⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡟⠀⠀⠀⠀⠀⠛⢿⣿⣿⣿⣿⣿⠂⠀⠀⠀⢀⡞⠁⠀⠀⠙⣆⠀⣀⡴⠾⠛⠛⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⢀⠀⠀⠉⠛⠿⢿⣿⣧⡀⠀⠀⡾⠀⠀⠀⠀⠀⣸⡾⠋⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠰⣽⣿⣿⠀⣸⠇⠀⠀⠀⢀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠚⠉⣿⣿⣇⠀⠀⠀⢸uwu⠀⠀⠀⢠⣿⡟⠁⢠⡟⠀⠀⠀⢠⡾⠁⠀⠀⠀⠀⣼⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠻⠟⢿⠀⠀⠀⣼esa⠀⠐⠒⣿⡏⠀⠀⣼⠃⠀⠀⣰⡟⠀⠀⠀⠀⠀⣸⣿⡄⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⣽⣧⠀⠀⣿⠀⠀⣼⠏⠀⠀⠀⠀⠀⢠⣿⢿⡿⡄⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢀⣴⣷⠀⠀⠀⠀⠀⠀⢿⣿⡄⢸⡇⠀⣼⠃⠀⠀⠀⠀⠀⠀⣾⡏⠀⢻⡹⣦⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⢸⡟⣿⡄⠀⠀⠀⠀⠀⠘⣿⣷⣾⣧⡞⠁⠀⠀⠀⠀⠀⠀⣸⠛⢧⠀⠀⢷⡘⢷⡄⠀⠀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⣾⠀⠘⣷⡀⠀⠀⠀⠀⠀⠈⠉⠙⠋⠀⠀⠀⠀⠀⠀⠀⣰⡏⠀⠈⢳⡄⠈⢳⡌⢻⡄⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⢀⡇⠀⠀⠈⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⣾⡅⠀⠀⠙⢿⣿⠀⠀⠘⢧⡀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣸⠀⠀⠀⠀⢸⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠸⣿⣧⣀⣀⡀⠀⣿⠀⠀⠀⠀⠹⣦⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢠⡏⠀⠀⣀⣀⣸⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⠀⠀⠀⠘⢿⣏⠻⢿⣾⣿⣦⣄⠀⠀⠀⠘⢧⡀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⣼⠁⠀⠛⠛⠿⠿⠿⠿⠃⠻⣿⣶⣄⡀⠀⠀⢀⣠⣶⡿⠃⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠙⢿⣿⡟⠻⣷⣦⡀⠀⣿⣦⣄⡀⠀
        ⢀⣠⡤⠴⠒⠒⠒⠒⢋⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⣿⣿⡿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⢻⣿⡀⠀⠙⢿⣦⣽⣿⣿⡿⠆
        ⠀⠀⠉⠉⠉⠒⠚⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀⠉⠉⠉⠁⠀⠀
__________________________________________________________________________________________________________________________
"""
