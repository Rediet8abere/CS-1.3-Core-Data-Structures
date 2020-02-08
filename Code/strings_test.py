#!python

import strings
import unittest


class StringsTest(unittest.TestCase):


    def test_StringMan_instance(self):
        self.check = strings.StringMan()
        assert self.check

    def test_contains_with_matching_patterns(self):
        check = strings.StringMan()
        # Positive test cases (examples) with matching patterns
        assert check.contains('abc', '') is True  # all strings contain empty string
        assert check.contains('abc', 'a') is True  # single letters are easy
        assert check.contains('abc', 'b') is True
        assert check.contains('abc', 'c') is True
        assert check.contains('abc', 'ab') is True  # multiple letters are harder
        assert check.contains('abc', 'bc') is True
        assert check.contains('abc', 'abc') is True  # all strings contain themselves
        assert check.contains('aaa', 'a') is True  # multiple occurrences
        assert check.contains('aaa', 'aa') is True  # overlapping pattern
        # TODO: Write more positive test cases with assert is True statements
        assert check.contains('..', '.') is True
        assert check.contains('../n', './n') is True
        assert check.contains('Rediet', 'Redi') is True
        assert check.contains('ooooooooohhhhh', 'oooohhhhh') is True

    def test_contains_with_non_matching_patterns(self):
        check = strings.StringMan()
        # Negative test cases (counterexamples) with non-matching patterns
        assert check.contains('abc', 'z') is False  # remember to test other letters
        assert check.contains('abc', 'ac') is False  # important to test close cases
        assert check.contains('abc', 'az') is False  # first letter, but not last
        assert check.contains('abc', 'abz') is False  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is False statements
        assert check.contains('btzze', 'tze') is False
        assert check.contains('aaa', 'a:''') is False
        assert check.contains('greek', 'eik') is False
        assert check.contains('hahahaha', 'hha') is False
    #
    def test_contains_with_complex_patterns(self):
        check = strings.StringMan()
        # Difficult test cases (examples) with complex patterns
        assert check.contains('ababc', 'ab') is True  # multiple occurrences
        assert check.contains('banana', 'na') is True  # multiple occurrences
        assert check.contains('ababc', 'abc') is True  # overlapping prefix
        assert check.contains('bananas', 'nas') is True  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        assert check.contains('hahahahahahaha', 'ha') is True
        assert check.contains('ooooooooohhhhh', 'oooohhh') is True
    #
    def test_find_index_with_matching_patterns(self):
        check = strings.StringMan()
        # Positive test cases (examples) with matching patterns
        assert check.find_index('abc', '') == 0  # all strings contain empty string
        assert check.find_index('abc', 'a') == 0  # single letters are easy
        assert check.find_index('abc', 'b') == 1
        assert check.find_index('abc', 'c') == 2
        assert check.find_index('abc', 'ab') == 0  # multiple letters are harder
        assert check.find_index('abc', 'bc') == 1
        assert check.find_index('abc', 'abc') == 0  # all strings contain themselves
        assert check.find_index('aaa', 'a') == 0  # multiple occurrences
        assert check.find_index('aaa', 'aa') == 0  # overlapping pattern
        # TODO: Write more positive test cases with assert equal int statements
        assert check.find_index('hahahahahahaha', 'ha') == 0
        assert check.find_index('bbc', 'bbc') == 0
    #
    def test_find_index_with_non_matching_patterns(self):
        check = strings.StringMan()
        # Negative test cases (counterexamples) with non-matching patterns
        assert check.find_index('abc', 'z') is None  # remember to test other letters
        assert check.find_index('abc', 'ac') is None  # important to test close cases
        assert check.find_index('abc', 'az') is None  # first letter, but not last
        assert check.find_index('abc', 'abz') is None  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is None statements
        assert check.find_index('bbc', 'bcc') is None
    #
    def test_find_index_with_complex_patterns(self):
        check = strings.StringMan()
        # Difficult test cases (examples) with complex patterns
        assert check.find_index('ababc', 'abc') == 2  # overlapping prefix
        assert check.find_index('bananas', 'nas') == 4  # overlapping prefix
        assert check.find_index('abcabcabc', 'abc') == 0  # multiple occurrences
        assert check.find_index('abcabcab', 'abc') == 0  # multiple occurrences
        assert check.find_index('abcabcdef', 'abcd') == 3  # overlapping prefix
        assert check.find_index('abcabcdef', 'abcdef') == 3  # overlapping prefix
        assert check.find_index('abcabcdabcde', 'abcde') == 7  # overlapping prefix
        assert check.find_index('abcabcdabcde', 'abcd') == 3  # multiple occurrences, overlapping prefix
        assert check.find_index('abra cadabra', 'abra') == 0  # multiple occurrences
        assert check.find_index('abra cadabra', 'adab') == 6  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        assert check.find_index('aaaahahahahaha', 'ha') == 4
    #
    def test_find_all_indexes_with_matching_patterns(self):
        check = strings.StringMan()
        # Positive test cases (examples) with matching patterns
        assert check.find_all_indexes('abc', '') == [0, 1, 2]  # all strings contain empty string
        assert check.find_all_indexes('abc', 'a') == [0]  # single letters are easy
        assert check.find_all_indexes('abc', 'b') == [1]
        assert check.find_all_indexes('abc', 'c') == [2]
        assert check.find_all_indexes('abc', 'ab') == [0]  # multiple letters are harder
        assert check.find_all_indexes('abc', 'bc') == [1]
        assert check.find_all_indexes('abc', 'abc') == [0]  # all strings contain themselves
        assert check.find_all_indexes('aaa', 'a') == [0, 1, 2]  # multiple occurrences
        assert check.find_all_indexes('aaa', 'aa') == [0, 1]  # overlapping pattern
    #     # TODO: Write more positive test cases with assert equal list statements
        assert check.find_all_indexes('hahahahahahaha', 'ha') == [0, 2, 4, 6, 8, 10, 12]
        assert check.find_all_indexes('hahahahahahaha', 'haha') == [0, 2, 4, 6, 8, 10]
    #
    #
    def test_find_all_indexes_with_non_matching_patterns(self):
        check = strings.StringMan()
    #     # Negative test cases (counterexamples) with non-matching patterns
        assert check.find_all_indexes('abc', 'z') == []  # remember to test other letters
        assert check.find_all_indexes('abc', 'ac') == []  # important to test close cases
        assert check.find_all_indexes('abc', 'az') == []  # first letter, but not last
        assert check.find_all_indexes('abc', 'abz') == []  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert equal list statements
        assert check.find_all_indexes('abra ca da bra', 'adab') == []

    #
    def test_find_all_indexes_with_complex_patterns(self):
        check = strings.StringMan()
        # Difficult test cases (examples) with complex patterns
        assert check.find_all_indexes('ababc', 'abc') == [2]  # overlapping prefix
        assert check.find_all_indexes('bananas', 'nas') == [4]  # overlapping prefix
        assert check.find_all_indexes('abcabcabc', 'abc') == [0, 3, 6]  # multiple occurrences
        assert check.find_all_indexes('abcabcab', 'abc') == [0, 3]  # multiple occurrences
        assert check.find_all_indexes('abcabcdef', 'abcd') == [3]  # overlapping prefix
        assert check.find_all_indexes('abcabcdef', 'abcdef') == [3]  # overlapping prefix
        assert check.find_all_indexes('abcabcdabcde', 'abcde') == [7]  # overlapping prefix
        assert check.find_all_indexes('abcabcdabcde', 'abcd') == [3, 7]  # multiple occurrences, overlapping prefix
        assert check.find_all_indexes('abra cadabra', 'abra') == [0, 8]  # multiple occurrences
        assert check.find_all_indexes('abra cadabra', 'adab') == [6]  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        assert check.find_all_indexes('ab cab cabc', 'abc') == [8]


if __name__ == '__main__':
    unittest.main()
