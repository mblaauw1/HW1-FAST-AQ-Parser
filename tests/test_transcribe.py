# write tests for transcribe functions
import pytest
import re
import math
from random import randint
#from parse import (FastaParser, FastqParser)

from seqparser import (
        transcribe,
        reverse_transcribe, FastaParser,FastqParser)

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()

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

def test_transcribe(test_data_fa,test_data_fq):
    #fasta
    parser_obj=FastaParser(test_data_fa)
    file_lines = [record for record in parser_obj]
    max_distance=len(file_lines)-1
    random_spot=randint(0,max_distance)
    random_position=file_lines[random_spot]
    sequence_random_position=random_position[1]
    #half_length = len(sequence_random_position)/2
    #rounded_number=round_half_up(half_length)
    
    
    transcription=transcribe(sequence_random_position)
    #print(transcription[10])
    if len(sequence_random_position)>0:
        max_distance=len(sequence_random_position)-1
        random_nucleotide_spot=randint(0,max_distance)
        print(random_nucleotide_spot)
        print(TRANSCRIPTION_MAPPING.get(sequence_random_position[random_nucleotide_spot],""))
        random_nucleotide=transcription[random_nucleotide_spot]
        actual_nucleotide=TRANSCRIPTION_MAPPING.get(sequence_random_position[random_nucleotide_spot],"")
        assert random_nucleotide==actual_nucleotide
        
    
    #fastq
    parser_obj=FastqParser(test_data_fq)
    file_lines = [record for record in parser_obj]
    max_distance=len(file_lines)-1
    random_spot=randint(0,max_distance)
    random_position=file_lines[random_spot]
    sequence_random_position=random_position[1]
    #half_length = len(sequence_random_position)/2
    #rounded_number=round_half_up(half_length)
    
    
    transcription=transcribe(sequence_random_position)
    #print(transcription[10])
    if len(sequence_random_position)>0:
        max_distance=len(sequence_random_position)-1
        random_nucleotide_spot=randint(0,max_distance)
        print(random_nucleotide_spot)
        print(TRANSCRIPTION_MAPPING.get(sequence_random_position[random_nucleotide_spot],""))
        random_nucleotide=transcription[random_nucleotide_spot]
        actual_nucleotide=TRANSCRIPTION_MAPPING.get(sequence_random_position[random_nucleotide_spot],"")
        assert random_nucleotide==actual_nucleotide
        
    pass

def test_reverse_transcribe(test_data_fa,test_data_fq):
    #fasta
    parser_obj=FastaParser(test_data_fa)
    file_lines = [record for record in parser_obj]
    max_distance=len(file_lines)-1
    random_spot=randint(0,max_distance)
    random_position=file_lines[random_spot]
    sequence_random_position=random_position[1]
    #half_length = len(sequence_random_position)/2
    #rounded_number=round_half_up(half_length)
    
    
    reverse_transcription=reverse_transcribe(sequence_random_position)
    print(sequence_random_position)
    print(reverse_transcription)
    if len(sequence_random_position)>0:
        max_distance=len(sequence_random_position)-1
        random_nucleotide_spot=randint(0,max_distance)
        print(random_nucleotide_spot)
        print(TRANSCRIPTION_MAPPING.get(sequence_random_position[max_distance-random_nucleotide_spot],""))
        random_nucleotide=reverse_transcription[random_nucleotide_spot]
        print(random_nucleotide)
        #print(random_nucleotide)
        actual_nucleotide=TRANSCRIPTION_MAPPING.get((sequence_random_position[max_distance-random_nucleotide_spot]),"")
        assert random_nucleotide==actual_nucleotide
        
    #fastq
    parser_obj=FastqParser(test_data_fq)
    file_lines = [record for record in parser_obj]
    max_distance=len(file_lines)-1
    random_spot=randint(0,max_distance)
    random_position=file_lines[random_spot]
    sequence_random_position=random_position[1]
    #half_length = len(sequence_random_position)/2
    #rounded_number=round_half_up(half_length)
    
    
    reverse_transcription=reverse_transcribe(sequence_random_position)
    #print(transcription[10])
    if len(sequence_random_position)>0:
        max_distance=len(sequence_random_position)-1
        random_nucleotide_spot=randint(0,max_distance)
        print(random_nucleotide_spot)
        print(TRANSCRIPTION_MAPPING.get(sequence_random_position[max_distance-random_nucleotide_spot],""))
        random_nucleotide=reverse_transcription[random_nucleotide_spot]
        actual_nucleotide=TRANSCRIPTION_MAPPING.get(sequence_random_position[max_distance-random_nucleotide_spot],"")
        assert random_nucleotide==actual_nucleotide
        
    pass

test_transcribe('data/test.fa','data/test.fq')
test_reverse_transcribe('data/test.fa','data/test.fq')