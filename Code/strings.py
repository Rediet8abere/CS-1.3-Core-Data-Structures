#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    index = 0
    count = 0
    indexP = []
    if len(pattern) == 0:
        print("Hi")
        return True
    print("lenT", len(text))
    print("lenP", len(pattern))

    for i in range(len(text)):
        print("checkinmg", pattern[index], text[i], pattern[index] == text[i])
        if index < (len(pattern)-1):
            if text[i] == pattern[index]:
                index += 1
            elif text[i] != pattern[index]:
                index = 0
        elif index == (len(pattern)-1) and pattern[index] == text[i]:
            # print("index", index, "(len(pattern)-1)", (len(pattern)-1))
            count += 1
            index = 0
            # print("pattern[index]", pattern[index], "text[i]", text[i])
    if count == 0:
        return False
    # print("count", count)
    return True



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    index = 0
    count = 0
    for i in range(len(text)):
        if index < (len(pattern)-1):
            if text[i] == pattern[index]:
                return i
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_all_indexes here (iteratively and/or recursively)
    indexes = []
    index = 0
    count = 0
    for i in range(len(text)):
        if index < (len(pattern)-1):
            if text[i] == pattern[index]:
                index += 1
            elif text[i] != pattern[index]:
                index = 0
        elif index == (len(pattern)-1) and len(pattern) != (1 or 2):
            count += 1
            indexes.append(((i+1)-len(pattern)))
            index = 0
    if count == 0:
        return []
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
