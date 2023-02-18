import re
from art import tprint
from markov_player.markov_player import MarkovPlayer


class UserInterface:
    def __init__(self, player: MarkovPlayer = MarkovPlayer()):
        self._player = player
        self._filename = None
        self._trie_initiated = False
        self._melody_length = 250

        self._start_controller = {
            "i": self._initiate_markov,
            "s": self._play_menu,
            "g": self._generate_music,
            "l": self._set_melody_length,
        }
        self._start_menu()
        self._trie_initiated = False

    def _set_melody_length(self):
        try:
            self._melody_length = int(
                input("Please insert the music file length (Recommended 250-500): ")
            )
            print("Music file length has been set successfully.")
        except ValueError as exc:
            print(f"Setting music file length has failed: {exc}")

    def _start_menu(self):
        print(
            """______________________________________________________________________________________"""
        )
        tprint("Music Generator")
        self._print_picture()
        while True:
            print(self._start_commands())
            key = str(input("Command: "))
            print(
                """______________________________________________________________________________________"""
            )
            if key == "e":
                break
            try:
                func = self._start_controller[key]
                func()
            except KeyError as exc:
                print(f"Incorrect command: {exc}")

    def _load_player(self):
        try:
            self._player.load_music(self._filename)
            return True
        except Exception as exc:
            print(f"File {self._filename} not found: {exc}")
            self._filename = None
            return False

    def _play_menu(self):
        playing = True
        self._print_picture()
        if (self._filename or self._filename == "") and self._load_player():
            self._player.play_music()
            while True:
                print(self._play_commands())
                key = input("Command: ")
                if key == "p" and playing:
                    self._player.pause_music()
                    playing = False
                elif key == "p" and not playing:
                    self._player.resume_music()
                    playing = True
                elif key == "c":
                    self._insert_filename()
                    self._play_menu()
                    break
                elif key == "x":
                    self._player.stop_music()
                    self._filename = None
                    break
        else:
            print()
            print("FileNotFound: Please insert a music filename.")
            self._insert_filename()
            self._play_menu()
            return

    def _insert_filename(self) -> str:
        print()
        self._filename = input("Filename (wav) : ")

    def _start_commands(self) -> str:
        return """
______________________________________________________________________________________

> i to initiate music player with data files.
> l to set the lenght of the music file.
> g to generate a new music file.
> s to start the music!
> e to exit.
______________________________________________________________________________________
"""

    def _play_commands(self) -> str:
        return """
______________________________________________________________________________________

> p to pause/unpause. 
> c to change the music file.
> x to exit back to the main menu.
______________________________________________________________________________________
"""

    def _print_picture(self) -> print:
        tprint("Music Generator")
        return print(
            self._beauty(),
        )

    def _depth_handler(self):
        depth = (
            input(
                "Please select a depth for the trie data structure (Optional, Defaults to 2): "
            )
            or 2
        )
        depth = int(depth)
        if depth <= 0:
            raise ValueError("Value must be integer larger than 0. Please try again.")
        return depth

    def _initiate_markov(self):
        try:
            print()
            depth = self._depth_handler()
        except ValueError as exc:
            print()
            print(f"{exc}")
            return

        try:
            self._player.initiate_markov(depth)
            self._trie_initiated = True
        except FileNotFoundError:
            print()
            print("FileNotFoundError: Data files not found.")
            print("Please insert Data Files to the Data folder, and try again.")

    def _generate_music(self):
        print()
        if not self._trie_initiated:
            print("GenerationError: Please iniatiate music player with data files.")
            return

        try:
            filename = str(input("Insert a name for the music file: "))
            prefix_notes = (
                str(input("Insert prefix notes in format; '2;121;22;11' (Optional): "))
                or None
            )
            depth = self._depth_handler()
            self._filename = filename
        except ValueError as exc:
            print(f"{exc}")
            return

        if self._prefix_validation(prefix_notes):
            self._player.generate_music(
                filename=filename,
                prefix_notes=prefix_notes,
                depth=depth,
                melody_length=self._melody_length,
            )
        else:
            print(
                "Prefix notes must be a sequence of integers between 1 and 127, separated by semicolons."
            )
            print("Example: '1;123;104;67;22'")

    def _prefix_validation(self, prefix_notes: str) -> bool:
        if prefix_notes:
            regex = r"""^(?:(?:[1-9]|[1-9][0-9]|1[0-1][0-9]|
            12[0-7]);)*(?:[1-9]|[1-9][0-9]|1[0-1][0-9]|12[0-7])$"""
            return re.match(regex, prefix_notes) is not None
        return True

    def _beauty(self):
        return """
                        ⢀⣤⣴⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⡿⠛⢻⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⠇⢀⣸⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⡟⠉⠀⠀⠀⢻⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠿⠣⡀⠀⠒⣶⣿⣿⣿⡏⢿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠏⠀⠀⠀⢸⣶⣶⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡟⠀⠀⠀⠀⠀⠛⢿⣿⣿⣿⣿⣿⠂⠀⠀⠀⢀⡞⠁⠀⠀⠙⣆⠀⣀⡴⠾⠛⠛⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⢀⠀⠀⠉⠛⠿⢿⣿⣧⡀⠀⠀⡾⠀⠀⠀⠀⠀⣸⡾⠋⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠰⣽⣿⣿⠀⣸⠇⠀⠀⠀⢀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠚⠉⣿⣿⣇⠀⠀⠀⢸   ⠀⠀⠀⢠⣿⡟⠁⢠⡟⠀⠀⠀⢠⡾⠁⠀⠀⠀⠀⣼⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠻⠟⢿⠀⠀⠀⣼   ⠀⠐⠒⣿⡏⠀⠀⣼⠃⠀⠀⣰⡟⠀⠀⠀⠀⠀⣸⣿⡄⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
"""
