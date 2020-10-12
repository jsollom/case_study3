import re
import time


def string_match_performance(filename, terms, case_insensitive=False):
    """
    Do a simple string match.
    
    Args:
      filename (string): Name of the file to search
      term (string): Term to search for
      case_insensitive (bool): True -- Do not consider case
                               False -- Consider case
    
    Returns:
      Number of matches (integer)
    
    Raises:
        VauleError if the term is empty
    """
    matches = 0
    results = []
    for term in terms:
        with open(filename, 'r') as fin:
            start = time.time()
            for line in fin:
                # Eliminate punctuation around words
                words = re.sub('[,.!?;]', '', line).split()
                for word in words:
                    if not case_insensitive:
                        if term == word:
                            matches += 1
                    else:
                        if term.lower() == word.lower():
                            matches += 1
            stop = time.time()
            results.append(stop - start)
    return results

