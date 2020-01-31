#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text, 0, len(text)-1)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # print("text", text)
    text = text.lower()
    index = len(text) - 1
    for i in range(len(text)):
        if text[i].isalpha() and text[index].isalpha():
            if text[i] == text[index]:
                index -= 1
            else:
                return False
        else:
            pass
    return True

    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    length = right
    text = text.lower()
    i = left
    index = right

    if index > 0:
        if text[i].isalpha() and text[index].isalpha():
            if text[i] == text[index]:
                if  i < length and index > 0:
                    i += 1
                    index -= 1
                    return is_palindrome_recursive(text, left=i, right=index)
                else:
                    return True
            else:
                return False
        elif text[i].isalpha() == False and i < length:
            i += 1
            return is_palindrome_recursive(text, left=i, right=index)
        elif text[index].isalpha() == False and index > 0:
            index -= 1
            return is_palindrome_recursive(text, left=i, right=index)
    return True

    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
