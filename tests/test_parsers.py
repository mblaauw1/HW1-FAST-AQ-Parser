
# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)
fa_data = open('/Users/maddieblaauw/Downloads/HW1-FAST-AQ-Parser-main/data/test.fa', "r")
fa_data=fa_data.read
fq_data = open('/Users/maddieblaauw/Downloads/HW1-FAST-AQ-Parser-main/data/test.fq', "r")
fq_data=fq_data.read

import pytest
import re
from random import randint

def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser(test_data):
    num_A=0
    num_C=0
    num_T=0
    num_G=0
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    line=randint(0,1000)
    FastaParser(test_data)
    get_record('/Users/maddieblaauw/Downloads/HW1-FAST-AQ-Parser-main/data/test.fa')
    
    #count all A, C, T, G and add; check to see if it equals the total length of the string
    if type(line)=="str":
        num_A=line.count('A')
        num_C=line.count('C')
        num_T=line.count('T')
        num_G=line.count('G')
    print(line)
    assert num_A+num_C+num_T+num_G == len(line)
  
    pass

def test_FastaFormat(test_data):
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    line=randint(0,1000)
    FastaParser(test_data)
    if seq_name=="None":
        assert True
    else: 
        print ("fail")
   
    pass


def test_FastqParser(test_data):
    num_A=0
    num_C=0
    num_T=0
    num_G=0
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    line=randint(0,1000)
    FastqParser(test_data)
    #count all A, C, T, G and add; check to see if it equals the total length of the string
    if type(line)=="str":
        num_A=line.count('A')
        num_C=line.count('C')
        num_T=line.count('T')
        num_G=line.count('G')
    assert num_A+num_C+num_T+num_G == len(seq)
  
    pass



def test_FastqFormat(test_data):
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    line=randint(0,1000)
    FastqParser(test_data)
    if seq_name=="None":
        assert True
    else: 
        print ("fail")
    pass

