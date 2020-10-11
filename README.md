Case Study #3: Document Search

This is my response to the Document Search case study.

# Installation

1. Clone this repository into a directory on your machine.
   git clone <>

2. Ensure that python is installed on your machine. Python 2.X has been deprecated since 2020; however, this code should run
   under either Python 2.X or 3.X.
   A. You can downloaded Python here: https://www.python.org/downloads/
   B. Alternately, there are installation instructions for installing Python 3 on the Mac here: https://docs.python-guide.org/starting/install3/osx/

# Usage

## Search tool 
1. Change directory to word_search/src/word_search.
   cd word_search/src/word_search

2. You can run the code by invoking 'search.py'.  

   IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT 

   Please set and export the PYTHONPATH variable to be the top of your word_search directory. 
   I have organized the code as I would a development project, but because it is not being installed on your system, you need to set the PYTHONPATH.

   export PYTHONPATH=<path-to>/word_search

   Note: There are two word_search directories. You want the top level one.

    word_search/
    ├── src
    │   └── word_search

   IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT 

   search.py

### Example invocation Python 2.7:

#### Full help due to '-h' invocation
$ python2.7 search.py -h
usage: search.py [-h] --operation {1,2,3} [-c] --files FILES [FILES ...] term

Search for a term in a text file

positional arguments:
  term                  Search term

optional arguments:
  -h, --help            show this help message and exit
  --operation {1,2,3}   1 -- Simple string match 2 -- Regular expression match
                        3 -- Indexed search
  -c, --case-insensitive
                        If specified, makes the search case insensitive.
  --files FILES [FILES ...]
                        Space separate list of text files to search   

#### Abbreviated help due to too few arguments
$ python2.7 search.py
usage: search.py [-h] --operation {1,2,3} [-c] --files FILES [FILES ...] term
search.py: error: too few arguments

#### Search for the word 'warp' using method 1 (Simple String Match) with case-insensitivity option
$ python2.7 search.py warp --operation 1 -c --files ../../test/sample_text/warp_drive.txt
../../test/sample_text/warp_drive.txt - 6 matches

#### Search for the word 'warp' using method 1 (Simple String Match) WITHOUT case-insensitivity option
$ python2.7 search.py warp --operation 1 --files ../../test/sample_text/warp_drive.txt
../../test/sample_text/warp_drive.txt - 5 matches

#### Search for the word 'warp' using method 1 (Regex Match) with case-insensitivity option
$ python2.7 search.py warp --operation 2 -c --files ../../test/sample_text/warp_drive.txt
../../test/sample_text/warp_drive.txt - 6 matches

#### Search for the word 'warp' using method 1 (Regex Match) WITHOUT case-insensitivity option
$ python2.7 search.py warp --operation 2 --files ../../test/sample_text/warp_drive.txt
../../test/sample_text/warp_drive.txt - 5 matches

#### Search for the word 'warp' using method 1 (Index Match) with case-insensitivity option
$ python2.7 search.py warp --operation 3 -c --files ../../test/sample_text/warp_drive.txt
../../test/sample_text/warp_drive.txt - 6 matches

#### Search for the word 'warp' using method 1 (Index Match) WITHOUT case-insensitivity option
$ python2.7 search.py warp --operation 3 --files ../../test/sample_text/warp_drive.txt
../../test/sample_text/warp_drive.txt - 5 matches

### Example Invocation with Python 3

#### Full help due to '-h' invocation
$ python2.7 search.py -h
usage: search.py [-h] --operation {1,2,3} [-c] --files FILES [FILES ...] term

Search for a term in a text file

positional arguments:
  term                  Search term

optional arguments:
  -h, --help            show this help message and exit
  --operation {1,2,3}   1 -- Simple string match 2 -- Regular expression match
                        3 -- Indexed search
  -c, --case-insensitive
                        If specified, makes the search case insensitive.
  --files FILES [FILES ...]
                        Space separate list of text files to search
$ python search.py -h
usage: search.py [-h] --operation {1,2,3} [-c] --files FILES [FILES ...] term

Search for a term in a text file

positional arguments:
  term                  Search term

optional arguments:
  -h, --help            show this help message and exit
  --operation {1,2,3}   1 -- Simple string match 2 -- Regular expression match 3 -- Indexed search
  -c, --case-insensitive
                        If specified, makes the search case insensitive.
  --files FILES [FILES ...]
                        Space separate list of text files to search

#### Abbreviated help due to too few arguments
$ python search.py
usage: search.py [-h] --operation {1,2,3} [-c] --files FILES [FILES ...] term
search.py: error: the following arguments are required: term, --operation, --files

#### Search for the word 'warp' using method 1 (Simple String Match) with case-insensitivity option
$ python search.py warp --operation 1 -c --files ../../test/sample_text/warp_drive.txt
../../test/sample_text/warp_drive.txt - 6 matches

#### Search for the word 'warp' using method 1 (Simple String Match) WITHOUT case-insensitivity option
$ python search.py warp --operation 1 --files ../../test/sample_text/warp_drive.txt
../../test/sample_text/warp_drive.txt - 5 matches

#### Search for the word 'warp' using method 1 (Regex Match) with case-insensitivity option
$ python search.py warp --operation 2 -c --files ../../test/sample_text/warp_drive.txt
../../test/sample_text/warp_drive.txt - 6 matches

#### Search for the word 'warp' using method 1 (Regex Match) WITHOUT case-insensitivity option
$ python search.py warp --operation 2 --files ../../test/sample_text/warp_drive.txt
../../test/sample_text/warp_drive.txt - 5 matches

#### Search for the word 'warp' using method 1 (Index Match) with case-insensitivity option
$ python search.py warp --operation 3 -c --files ../../test/sample_text/warp_drive.txt
../../test/sample_text/warp_drive.txt - 6 matches

#### Search for the word 'warp' using method 1 (Index Match) WITHOUT case-insensitivity option
$ python search.py warp --operation 3 --files ../../test/sample_text/warp_drive.txt
../../test/sample_text/warp_drive.txt - 5 matches

## Unit Tests

You can run unit tests, but you will need to install pytest first. I suggest doing so inside a
Virtual environment.

1. Change directory to the top level
   cd <path-to>/word_search

2. Create virtual environment
   python -m venv .venv

3. Activate virtual environment
   . .venv/bin/activate

   Note: You should see your prompt change to (.venv).

4. pip install -r test/requirements.txt
   Note: You will likely get a warning about upgrading pip.

5. Run the unit tests.
   pytest

   You should see output like this.
============================================================================================================================ test session starts =============================================================================================================================
platform darwin -- Python 3.8.5, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /Users/jasons/eclipse-workspace/word_search
collected 12 items

test/test_match.py ............                                                                                                                                                                                                                                        [100%]

============================================================================================================================= 12 passed in 0.07s =============================================================================================================================
  You can run pytest with multiple '-v's to get more output.

## Performance Test

You can run the performance test, but it is set to run through all three methods serially which can take more than two hours to run.
I used a file words_alpha.txt that contains 370102 English words. I ran through it 6 times for each search algorithm which is 
2220612 times, so a little over 2 million searches. I wanted each algorithm to get the same words, so that it was an apples-to-apples
comparison.

1. cd word_search/performance_test

2. performance_test.py