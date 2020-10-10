#! /usr/bin/env python

"""
This program accepts a search term, a method for searching, and the
file in which to search.

It prints out the number of occurrencs
"""

import argparse
import sys

from src.word_search.string_match import string_match
from src.word_search.regex_match import regex_match
from src.word_search.index_match import index_match

FUNC_MAP = {1: string_match,
            2: regex_match,
            3: index_match, }


def arguments(args):
    """
    Handle command line arguments
    """
    parser = argparse.ArgumentParser(
        description="Search for a term in a text file")
    parser.add_argument('term', type=str,
                        help='Search term')
    parser.add_argument('--operation',
                        required=True,
                        type=int,
                        choices=[1, 2, 3],
                        help='1 -- Simple string match\n'
                        '2 -- Regular expression match\n'
                        '3 -- Indexed search')
    parser.add_argument('-c', '--case-insensitive',
                        action='store_true',
                        default=False,
                        help='If specified, makes the search case insensitive.')
    parser.add_argument('--files', type=str,
                        nargs='+',
                        required=True,
                        help='Space separate list of text files to search')

    return parser.parse_args(args)


def main(in_args):
    args = arguments(in_args)
    file_relevance = {}
    for file in args.files:
        try:
            matches = FUNC_MAP[args.operation](file, args.term, args.case_insensitive)
            file_relevance[file] = matches
        except (FileNotFoundError, ValueError) as err:
            print("ERROR: {}".format(err))
            sys.exit(1)

    sort_orders = sorted(file_relevance.items(), key=lambda x: x[1], reverse=True)

    for i in sort_orders:
        print("{} - {} matches ".format(i[0], i[1]))


if "__main__" == __name__:
    main(sys.argv[1:])
