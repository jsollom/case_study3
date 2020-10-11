#! /usr/bin/env python

import datetime
import io
import sys

from src.word_search.search import main as search


def main(args):

    with open('words_alpha.txt', 'r') as fin:
        search_terms = fin.read().split()

    operation_times = {}
    # for operation in ['3', '2', '1']:
    for operation in ['3']:
        start = datetime.datetime.now()

        iteration = 6
        for i in range(iteration):
            print("Operation: {}\tIteration: {} of {}".format(operation, i, iteration))

            # create a text trap and redirect stdout
            text_trap = io.StringIO()
            sys.stdout = text_trap

            for term in search_terms:
                args = [term , '--operation', operation, '--files',
                        '../test/sample_text/warp_drive.txt',
                        '../test/sample_text/french_armed_forces.txt',
                        '../test/sample_text/hitchhikers.txt']
                search(args)
            # now restore stdout function
            sys.stdout = sys.__stdout__

        stop = datetime.datetime.now()
        operation_times[operation] = stop - start

    for k, v in operation_times.items():
        print("Operation {} Elapsed time: {}\n".format(k, v))


if "__main__" == __name__:
    main(sys.argv[1:])

