import re
import random
from markov_player.markov_player import MarkovPlayer


class UserInterface:
    def __init__(self, player: MarkovPlayer = MarkovPlayer()):
        self._player = player
        self._commands = {
            "pause": player.pause_music(),
            "resume": player.resume_music(),
            "stop": player.stop_music(),
        }
        self._trie_initiated = False
        self._start_menu()

    def _start_menu(self):
        while True:
            print(random.choice([self._first_notation(), self._second_notation()]))
            print(self._start_commands())
            key = input(": ")
            if key == "e":
                break
            elif key == "i":
                try:
                    depth = int(
                        input("Please select a depth for the trie data structure:")
                    )
                    self._setup_markov(depth)
                except ValueError:
                    print("Value must be integer. Please try again.")

            elif key == "s":
                self._music_menu()

            elif key == "g":
                filename = str(input("Insert a name for the music file:  "))
                prefix_notes = str(
                    input("Insert prefix notes in format; '2;121;22;11' (Optional):")
                )
                depth = int(
                    input(
                        "Insert the depth of the data to be used for generation (Optional, Defaults to 2) : "
                    )
                )
                if prefix_notes == "":
                    prefix_notes = None

    def _music_menu(self):
        while True:
            print(self._music_control_commands())
            key = input(": ")
            if key == "r":
                break

    def _start_commands(self) -> str:
        return """
:> i to initiate music player with data files.
:> g to generate a new music file.
:> s to switch to play menu.
:> e to exit.
"""

    def _music_control_commands(self) -> str:
        return """
:> p to play/pause. 
:> s to stop.
:> r to return to main menu.
"""

    def _setup_markov(self, depth: int):
        try:
            self._player.initiate_markov(depth)
        except FileNotFoundError:
            print("FileNotFoundError: Data files not found.")
            print("Please insert Data Files to the Data folder, and try again.")

    def _generate_music(
        self, filename: str, prefix_notes: str, depth: int, melody_length
    ):
        if self._prefix_validation(prefix_notes):
            self._player.generate_music(
                filename=filename,
                prefix_notes=prefix_notes,
                depth=depth,
                melody_length=melody_length,
            )
        else:
            print(
                "Prefix notes must be a sequence of integers between 1 and 127, separated by semicolons."
            )
            print("Example: '1;123;104;67;22'")

    def _prefix_validation(self, string):
        regex = r"^(?:(?:[1-9]|[1-9][0-9]|1[0-1][0-9]|12[0-7]);)*(?:[1-9]|[1-9][0-9]|1[0-1][0-9]|12[0-7])$"
        if re.match(regex, string):
            return True
        return False

    def _first_notation(self):
        return """
        =IY;           
      XRVRRi          
     =Ri :RR          
     VR  ;RR          
     RY  tRY          
     RX ;RR;          
     tR=RRR           
     ;RRRR;           
     ;RRRi            
    ;RRRV             
   ;RRRRR:            
  :RRRV.RX            
  VRRR: ;R=           
 =RRR+   YRitti;.     
 VRRR  :YRRRRRRRRt.   
.RRRY ;RRYYR;;iRRRR.  
:RRRi RR; .Rt  .XRRY  
:RRR= RV   +R.  .RRR  
:RRRt tR    Rt   IRR. 
 RRRR  ;;   +R.  XRY  
 ;RRRt      .R+ +RR:  
  ;RRRX;     YRIRX:   
   .+RRRRIiitRRY;     
      :;+ii+;tR:      
             ;R:      
             iR       
    ;VRRi    Vi       
    RRRRR.  tR.       
    YRRR+ ;YV:        
    .tRRRRR+          
      .;;:
"""

    def _second_notation(self) -> str:
        return """
             ;I;              
             +It.             
             +II+             
             +III;            
             +IIII;           
             iIIIII;          
             titIIII;         
             I;.iIIII;        
            .I;  =IIII;       
            .I;   ;IIII:      
            .I;    :tIIt      
            .I;     .tII=     
            .I;      :III     
            :I;       +II;    
            :I;       .II=    
            :I:        iIi    
            :I.        ;Ii    
            ;I.        =I;    
            ;I.        tt     
            +I        ;I;     
            +I       ;I;      
            tI      ;I;       
     :;itIIIII     +t:        
   ;tIIIIIIIII   :t;          
 .tIIIIIIIIIIi  ;i.           
.tIIIIIIIIIII;.;:             
;IIIIIIIIIII;                 
;IIIIIIIIIt;                  
 ;tIIIIt+;                    
   ....
    
    """
