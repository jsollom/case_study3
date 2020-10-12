#! /usr/bin/env python

import datetime
import io
import sys

from src.word_search.search import main as search
from string_match import string_match_performance
from regex_match import regex_match_performance
from index_match import index_match_performance


def main(args):

    results = {'warp': {},
               'french': {},
               'hitch': {}}
    with open('words_alpha.txt', 'r') as fin:
        search_terms = fin.read().split()

    for func in [string_match_performance,
                 regex_match_performance,
                 index_match_performance]:
        iteration = 6
        for i in range(iteration):
            print("Operation: {}\tIteration: {} of {}\tTime: {}".format(func.__name__,
                                                                        i,
                                                                        iteration,
                                                                        datetime.datetime.now()))

            results['warp'][iteration] = func("../test/sample_text/warp_drive.txt",
                                                                  search_terms,
                                                                  False)
            results['french'][iteration] = func("../test/sample_text/french_armed_forces.txt",
                                                                  search_terms,
                                                                  False)
            results['hitch'][iteration] = func("../test/sample_text/hitchhikers.txt",
                                                                  search_terms,
                                                                  False)

        # print(results)

        total = 0
        for term in ['warp', 'french', 'hitch']:
            for i in range(iteration):
                total += sum(results[term][iteration])
        print("{} Average: {}".format(func.__name__, total / (iteration * len(search_terms))))


if "__main__" == __name__:
    main(sys.argv[1:])

