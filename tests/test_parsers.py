# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest
import re

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

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    FastaParser(test.fa)
        line = raw_input("Please provide some info: ")
        if not re.match(" A C T G", line):
            print "Error! Only letters *space* A C T G allowed!"
            else assert True
            sys.exit()   
    pass

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """

    FastaParser(test.fq)
    if seq_name=="None"
        assert True
    else print "fail"
   
    pass


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    FastaParser(test.fq)
        line = raw_input("Please provide some info: ")
        if not re.match(" A C T G", seq):
            print "Error! Only letters *space* A C T G allowed!"
            else assert True
            sys.exit()   
    pass

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    FastqParser(test.fa)
    if seq_name=="None":
        assert True
    else: 
        print "fail"
    pass