#! /usr/bin/env python

"""
This program accepts a search term and a method for searching.
"""

import argparse
import json
import re
import sys


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


def string_match(filename, term, case_insensitive=False):
    """
    Do a simple string match
    
    Args:
      filename (string): Name of the file to search
      term (string): Term to search for
    """
    matches = 0
    with open(filename, 'r') as fin:
        for word in fin.read().split():
            if not case_insensitive:
                if term == word:
                    matches += 1
            else:
                if term.lower() == word.lower():
                    matches += 1

    return matches


def regex_match(filename, term, case_insensitive=False):
    """
    Search using regular expressions
    """
    if case_insensitive:
        prog = re.compile(term, flags=re.IGNORECASE)
    else:
        prog = re.compile(term)
    with open(filename, 'r') as fin:
        data = fin.read()
        matches = prog.findall(data)
    return len(matches)


def create_index(filename):
    """
    Index all of the words in a file.
    Save that index as a file.
    """
    index = {}
    case_insensitive_index = {}
    with open(filename, 'r') as fin:
        for word in fin.read().split():
            if word in index:
                index[word] += 1
            else:
                index[word] = 1
            if word.lower() in case_insensitive_index:
                case_insensitive_index[word.lower()] += 1
            else:
                case_insensitive_index[word.lower()] = 1
    return index, case_insensitive_index


def save_index(filename, index, ci_index):
    """
    Saves an index for a filename as filename.index.
    """
    with open("{}.index".format(filename), 'w') as fout:
        json_body = {'index': index,
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
    try:
        raise FileNotFoundError
        fin = open("{}.index".format(filename))
        json_payload = json.load(fin)
        return json_payload['index'], json_payload['ci_index']
    except FileNotFoundError:
        index, ci_index = create_index(filename)
        save_index(filename, index, ci_index)
        return index, ci_index


def index_match(filename, term, case_insensitive=False):
    """
    Create an index ahead of time. Then, just search the index
    for the term.
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
    pass


if "__main__" == __name__:
    main(sys.argv[1:])
