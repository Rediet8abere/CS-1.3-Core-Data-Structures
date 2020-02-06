#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    if len(pattern) == 0:
        return True
    index = 0
    i = 0
    while i < len(text):
        if index < len(pattern):
            if pattern[index] == text[i]:
                index += 1
                i += 1
                if index == len(pattern):
                    return True
            elif index != 0:
                i -= (index - 1)
                index = 0
            else:
                i += 1
        else:
            index = 0
            if pattern[index] == text[i]:
                index += 1
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    if len(pattern) == 0:
        return 0

    # if contains(text, pattern):
    index = 0
    i = 0
    while i < len(text):
        if index < len(pattern):
            if pattern[index] == text[i]:
                index += 1
                i += 1
                if index == len(pattern):
                    return i-len(pattern)
            elif index != 0:
                i -= (index - 1)
                index = 0
            else:
                i += 1
        else:
            index = 0
            if pattern[index] == text[i]:
                index += 1
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_all_indexes here (iteratively and/or recursively)
    print("len", len(text))
    indexes = []
    if len(pattern) == 0:
        for i in range(len(text)):
            indexes.append(i)
        return indexes
    index = 0
    i = 0
    while i < len(text):
        if pattern[index] == text[i]:
            index += 1
            i += 1
            if index == len(pattern):
                indexes.append(i-len(pattern))
                if len(pattern) != 1:
                    i -= (index - 1)
                index = 0
        elif index != 0:
            i -= (index - 1)
            index = 0
        else:
            i += 1
            index = 0
    return indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


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
