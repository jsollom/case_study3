import hashlib
import json
import os
import re
import time


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


def save_index(filename, index, ci_index):
    """
    Saves indices for a filename.
    """
    with open(filename, 'w') as fout:
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
    file = os.path.basename(filename)
    directory = os.path.dirname(filename)
    index_filename = "{}/.{}.index".format(directory, file)
    try:
        fin = open(index_filename)
        json_payload = json.load(fin)
        return json_payload['index'], json_payload['ci_index']
    except FileNotFoundError:
        index, ci_index = create_index(filename)
        save_index(index_filename, index, ci_index)
        return index, ci_index


def index_match_performance(filename, terms, case_insensitive=False):
    """
    Create an index, basically a dictionary where the words are the keys and
    the value are the number of occurrences of the word, ahead of time. 
    Then, just search the index for the term.
    
    Returns:
      Number of matches (integer)
    
    Raises:
        VauleError if the term is empty    
    """
    results = []
    for term in terms:
        start = time.time()
        index, ci_index = get_index(filename)
        if not case_insensitive:
            true_index = index
        else:
            true_index = ci_index
        if term in true_index:
            matches = true_index[term]
        else:
            matches = 0
        stop = time.time()
        results.append(stop - start)
    return results
