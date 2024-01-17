# write tests for transcribe functions
import pytest
import re


from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


#Rounding function
def round_half_up(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier + 0.5) / multiplier

def test_transcribe():
    #fasta
    FastaParser(test.fa)
    line=old_line
    transcribe(test.fa)
    if len(line)>0:
        nucleotide=old_line[round_half_up(old_line[len/2])]
        TRANSCRIPTION_MAPPING.get("nucleotide")
        assert nucleotide==line[round_half_up(old_line[len/2])]
        
    
    #fastq
    FastqParser(test.fq)
    seq=old_line
    transcribe(test.fq)
    if len(seq)>0:
        nucleotide=old_line[round_half_up(old_line[len/2])]
        TRANSCRIPTION_MAPPING.get("nucleotide")
        assert nucleotide==seq[round_half_up(old_line[len/2])]
        
    pass


def test_reverse_transcribe():
    #fasta
    FastaParser(test.fa)
    line=old_line
    reverse_transcribe(test.fa)
    if len(line)>0:
        nucleotide=old_line[round_half_up(len(line)/2)-round_half_up(old_line[len/2])]
        TRANSCRIPTION_MAPPING.get("nucleotide")
        assert nucleotide==line[round_half_up(len(line)/2)-round_half_up(old_line[len/2])]
    
    #fastq
    FastqParser(test.fq)
    seq=old_line
    reverse_transcribe(test.fq)
    if len(seq)>0:
        nucleotide=old_line[round_half_up(len(seq)/2)-round_half_up(old_line[len/2])]
        TRANSCRIPTION_MAPPING.get("nucleotide")
        assert nucleotide==seq[round_half_up(len(seq)/2)-round_half_up(old_line[len/2])]
    
    pass