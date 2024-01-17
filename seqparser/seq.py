# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    
    #length of string
    for x=range(len(line)):
        #at each position, look at nucleotide
        nucleotide = line[x]
        #switch
        line[x] = TRANSCRIPTION_MAPPING.get("nucleotide")
    pass

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    
        #length of string
    for x=range(len(seq)):
        #at each position, look at nucleotide
        nucleotide = seq[len(x)-x]
        #switch
        string_reverse[x] = TRANSCRIPTION_MAPPING.get("nucleotide")
    seq=string_reverse   
    pass
       

    # Hey this is my comment
    # Again!
    pass