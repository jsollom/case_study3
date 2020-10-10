import re


def string_match(filename, term, case_insensitive=False):
    """
    Do a simple string match.
    
    Args:
      filename (string): Name of the file to search
      term (string): Term to search for
      case_insensitive (bool): True -- Do not consider case
                               False -- Consider case
    
    Returns:
      Number of matches (integer)
    """
    matches = 0
    with open(filename, 'r') as fin:
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

    return matches

