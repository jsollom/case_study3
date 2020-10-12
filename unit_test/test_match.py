import os
import pytest

from src.word_search.string_match import string_match
from src.word_search.regex_match import regex_match
from src.word_search.index_match import index_match


class TestMatch():

    valid_functions = [string_match, regex_match, index_match]

    @pytest.mark.parametrize("func", valid_functions)
    def testInvalidFileName(self, func):
        with pytest.raises(FileNotFoundError):
            func('ImNotHere', 'foo', False)

    @pytest.mark.parametrize("func", valid_functions)
    def testMatchesCaseInsensitive(self, func):
        test_dir = os.path.dirname(os.getenv('PYTEST_CURRENT_TEST').split('::')[0])
        cwd = os.path.join(os.getcwd(), test_dir)

        # Search term is all lower case
        matches = string_match("{}/sample_text/warp_drive.txt".format(cwd),
                               'warp', True)
        assert matches == 6

        # Search term is mixed case
        matches = string_match("{}/sample_text/warp_drive.txt".format(cwd),
                               'WaRp', True)
        assert matches == 6

        # Numeric search term
        matches = string_match("{}/sample_text/warp_drive.txt".format(cwd),
                               '5', True)
        assert matches == 1

    @pytest.mark.parametrize("func", valid_functions)
    def testMatchesCaseSensitive(self, func):
        test_dir = os.path.dirname(os.getenv('PYTEST_CURRENT_TEST').split('::')[0])
        cwd = os.path.join(os.getcwd(), test_dir)
        matches = string_match("{}/sample_text/warp_drive.txt".format(cwd),
                               'warp', False)
        assert matches == 5

        # Numeric search term
        matches = string_match("{}/sample_text/warp_drive.txt".format(cwd),
                               '5', False)
        assert matches == 1

    @pytest.mark.parametrize("func", valid_functions)
    def testInputValidation(self, func):
        test_dir = os.path.dirname(os.getenv('PYTEST_CURRENT_TEST').split('::')[0])
        cwd = os.path.join(os.getcwd(), test_dir)

        # Empty search term
        with pytest.raises(ValueError):
            string_match("{}/sample_text/warp_drive.txt".format(cwd),
                                   '', False)

        # Extremely large search term
        matches = string_match("{}/sample_text/warp_drive.txt".format(cwd),
                               'abcd' * 1000, False)
        assert matches == 0

