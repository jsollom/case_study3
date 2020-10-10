#! /usr/bin/env python

"""
This program accepts a search term and a method for searching.
"""

import argparse
import hashlib
import json
import os
import re
import sys

from src.string_match import string_match


def arguments(args):
    """
    Handle command line arguments
    """
    parser = argparse.ArgumentParser(
        description="Search for a term in a text file")
    parser.add_argument('file', type=str,
                        help='Text file to search')
    parser.add_argument('term', type=str,
                        help='Search term')
    parser.add_argument('--operation',
                        required=True,
                        type=int,
                        choices=[1, 2, 3],
                        help='1 -- Simple string match\n'
                        '2 -- Regular expression\n'
                        '3 -- Indexed search')
    parser.add_argument('-c', '--case-insensitive',
                        action='store_true',
                        default=False,
                        help='If specified, makes the search case insensitive.')

    return parser.parse_args(args)


def regex_match(filename, term, case_insensitive=False):
    """
    Search using regular expressions
    
    Args:
      filename (string): Name of the file to search
      term (string): Term to search for
      case_insensitive (bool): True -- Do not consider case
                               False -- Consider case
    
    Returns:
      Number of matches (integer)
    """
    total_matches = 0
    if case_insensitive:
        prog = re.compile(term, flags=re.IGNORECASE)
    else:
        prog = re.compile(term)
    with open(filename, 'r') as fin:
        for line in fin:
            matches = prog.findall(line)
            total_matches += len(matches)
    return total_matches


def md5(fname):
    """
    Create an md5sum for the file.
    
    Copied from:
    https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
    
    Returns
        hex string representation for the digest
    """
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def create_index(filename):
    """
    Index all of the words in a file.

    Return
        Dictionary of all of the words in the file; 
          Keys are the words themselves.
          Values are the number of occurrences of that word in the file. 
        Same dictionary as above but of all of the words in the file are lower-cased
    """
    index = {}
    case_insensitive_index = {}
    with open(filename, 'r') as fin:
        for line in fin:
            # Eliminate punctuation around words
            words = re.sub('[,.!?;]', '', line).split()
            for word in words:
                if word in index:
                    index[word] += 1
                else:
                    index[word] = 1
                lc_word = word.lower()
                if lc_word in case_insensitive_index:
                    case_insensitive_index[lc_word] += 1
                else:
                    case_insensitive_index[lc_word] = 1
    return index, case_insensitive_index


def save_index(original_filename, index_filename, index, ci_index):
    """
    Saves indices for a filename.
    """
    with open(index_filename, 'w') as fout:
        md5sum = md5(original_filename)
        json_body = {'md5sum': md5sum,
                     'index': index,
                     'ci_index': ci_index}
        json.dump(json_body, fout)


def get_index(filename):
    """
    Return an index for a given file.
    If the index already exists, return it.
    If not, then create it.
    TODO: I should probably do some kind of safe load
    and not just json load it.
    TODO: I should do an md5sum comparison or something
    to ensure that I'm dealing with the same file I have
    previously indexed.
    """
    file = os.path.basename(filename)
    directory = os.path.dirname(filename)
    index_filename = "{}.{}.index".format(directory, file)
    try:
        fin = open(index_filename)
        json_payload = json.load(fin)
        if json_payload['md5sum'] == md5(filename):
            return json_payload['index'], json_payload['ci_index']
    except FileNotFoundError:
        pass
    # Fall through to this code either if the index file was not found
    # or if its md5sum did not match the existing index file.
    index, ci_index = create_index(filename)
    save_index(filename, index_filename, index, ci_index)
    return index, ci_index


def index_match(filename, term, case_insensitive=False):
    """
    Create an index, basically a dictionary where the words are the keys and
    the value are the number of occurrences of the word, ahead of time. 
    Then, just search the index for the term.
    """
    index, ci_index = get_index(filename)
    if not case_insensitive:
        true_index = index
    else:
        true_index = ci_index
    if term in true_index:
        return true_index[term]
    else:
        return 0


func_map = {1: string_match,
            2: regex_match,
            3: index_match, }


def main(in_args):
    args = arguments(in_args)
    matches = func_map[args.operation](args.file, args.term, args.case_insensitive)
    print("Matches: {}".format(matches))


if "__main__" == __name__:
    main(sys.argv[1:])
