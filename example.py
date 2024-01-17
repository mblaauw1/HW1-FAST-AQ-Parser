from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    # Create instance of FastqParser
    FastaParser(Parser)
    FastqParser(Parser)
    
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    transcribe(line)
    print(line)
    
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    transcribe(seq)
    print(seq)
    
    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    reverse(transcribe(line))
    print(line)
    
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    reverse(transcribe(seq))
    print(seq)

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
