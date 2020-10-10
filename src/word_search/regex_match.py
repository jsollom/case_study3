import re


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
    
    Raises:
        VauleError if the term is empty
    """
    if not term:
        raise ValueError('Search term was empty.')

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
