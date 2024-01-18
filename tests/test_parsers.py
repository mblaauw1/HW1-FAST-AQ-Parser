
# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest
import re
from random import randint
import math

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
    #line=randint(0,1000)
    parser_obj=FastaParser(test_data)
    file_lines = [record for record in parser_obj]
    max_distance=len(file_lines)-1
    random_spot=randint(0,max_distance)
    random_position=file_lines[random_spot]
    sequence_random_position=random_position[1]
    print(sequence_random_position)
    print(type(sequence_random_position))
    #count all A, C, T, G and add; check to see if it equals the total length of the string
    
    num_A=sequence_random_position.count('A')
    num_C=sequence_random_position.count('C')
    num_T=sequence_random_position.count('T')
    num_G=sequence_random_position.count('G')
    print(num_A)
    print(num_C)
    print(num_T)
    print(num_G)
    print(len(sequence_random_position))
    assert num_A+num_C+num_T+num_G == len(sequence_random_position)
  
    pass

def test_FastaFormat(test_data):
    parser_obj=FastaParser(test_data)
    file_lines = [record for record in parser_obj]
    max_distance=len(file_lines)-1
    random_spot=randint(0,max_distance)
    random_position=file_lines[random_spot]
    first_in_tuple_random_position=random_position[0]
    print(random_position)
    #print(file_lines)
    #print(file_lines)
    print(len(random_position))
    sub ='seq'+str(random_spot)
    print(sub)
    assert sub == first_in_tuple_random_position
    #if sub in first_in_tuple_random_position==True 
        #assert 1==1
    #elif os.path.getsize(test_data) == 0:
        #assert 1==1



def test_FastqParser(test_data):
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
    #line=randint(0,1000)
    parser_obj=FastqParser(test_data)
    file_lines = [record for record in parser_obj]
    max_distance=len(file_lines)-1
    random_spot=randint(0,max_distance)
    random_position=file_lines[random_spot]
    sequence_random_position=random_position[1]
    print(sequence_random_position)
    #print(type(sequence_random_position))
    #count all A, C, T, G and add; check to see if it equals the total length of the string
    
    num_A=sequence_random_position.count('A')
    num_C=sequence_random_position.count('C')
    num_T=sequence_random_position.count('T')
    num_G=sequence_random_position.count('G')
    print(num_A)
    print(num_C)
    print(num_T)
    print(num_G)
    print(len(sequence_random_position))
    assert num_A+num_C+num_T+num_G == len(sequence_random_position)
  
    pass



def test_FastqFormat(test_data):
    parser_obj=FastqParser(test_data)
    file_lines = [record for record in parser_obj]
    max_distance=len(file_lines)-1
    random_spot=randint(0,max_distance)
    random_position=file_lines[random_spot]
    first_in_tuple_random_position=random_position[0]
    print(first_in_tuple_random_position)
    #print(file_lines)
    print(type(first_in_tuple_random_position[0]))
    assert type(first_in_tuple_random_position[0])==str
    pass


test_FastaParser('data/test.fa')
test_FastaFormat('data/test.fa')
test_FastqParser('data/test.fq')
test_FastqFormat('data/test.fq')