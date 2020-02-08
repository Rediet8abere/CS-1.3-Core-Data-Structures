#!python
class StringMan:
    def __init__(self):
        self.indexes = []


    def contains(self, text, pattern):
        """Time-Space Complexity:
            Best Case: O(1) if pattern is an empty string we know an empty strings occur in a text
            Worst Case: O(n) we have to iterate through n number of text to check if a pattern exists"""
        if len(pattern) == 0:
            return True
        self.indexes = []
        self.find_all_indexes(text, pattern)
        return self.indexes != []

    def find_index(self, text, pattern):
        """Time-Space Complexity:
            Best Case: O(1) if pattern is an empty string we know an empty strings occur in a text at the first index
            Worst Case: O(n) we have to iterate through n number of text to check if a pattern exists"""
        if len(pattern) == 0:
            return 0
        self.indexes = []
        self.find_all_indexes(text, pattern)
        if len(self.indexes) >= 1:
            return self.indexes[0]
        else:
            return None

    def find_all_indexes(self, text, pattern):
        """Time-Space Complexity:
            Worst Case: O(n) we have to iterate through n number of text to check if a pattern exists or doesn't exist"""
        if len(pattern) == 0:
            for i in range(len(text)):
                self.indexes.append(i)
            return self.indexes
        self.indexes = []
        index = 0
        i = 0
        while i < len(text):
            if pattern[index] == text[i]:
                index += 1
                i += 1
                if index == len(pattern):
                    self.indexes.append(i-len(pattern))
                    if len(pattern) != 1:
                        i -= (index - 1)
                    index = 0
            elif index != 0:
                i -= (index - 1)
                index = 0
            else:
                i += 1
                index = 0
        return self.indexes

def test_string_algorithms(text, pattern):
    check = StringMan()

    print('contains({!r}, {!r}) => {}'.format(text, pattern, check.contains(text, pattern)))
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, check.find_index(text, pattern)))
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, check.find_all_indexes(text, pattern)))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
