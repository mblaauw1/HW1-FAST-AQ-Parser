# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(sequence: str, reverse: bool = False) -> str:
    transcription = ""
    for nucleotide in sequence:
        transcription += TRANSCRIPTION_MAPPING.get(nucleotide, "")
    return transcription

    pass

def reverse_transcribe(sequence: str) -> str:
    length_of_string = len(sequence)
    string_reverse = [''] * length_of_string
    for x in range(length_of_string):
        nucleotide = sequence[length_of_string - x - 1]
        string_reverse[x] = TRANSCRIPTION_MAPPING.get(nucleotide, "")
    return ''.join(string_reverse)
       

    # Hey this is my comment
    # Again!
    pass