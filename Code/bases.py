#!python

import string
import math
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Decode digits from binary (base 2)
    hexAlp = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20, 'L':21, 'M':22,
              'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}
    binary = []
    tobebin =[]
    bin = []
    sum = 0
    frac = ''
    sumFrac = 0
    if digits.isupper() or digits.islower():
        print("not ")
        if (digits.find('.')!=-1) == True:
            print("index", digits.index('.'))
            print("digits[:digits.index('.')]", digits[:digits.index('.')])
            number = digits[:digits.index('.')]
            frac += "0"+digits[digits.index('.'):]
            print("True")
        else:
            number = digits
    elif isinstance(float(digits), float) == True:
        print("floating")
        x = float(digits)
        frac += str(round(x-int(x), (len(digits)-1) - len(str(int(x)))))
        number = str(int(float(digits)))
    print("fraction decoding", frac)



    for i in range(len(number)):
        # multipying each palce with it's digit place value
        if number[len(number)-(i+1)].isdigit():
            sum += int(number[len(number)-(i+1)])*(base**i)
        else:
            sum += hexAlp.get(number[len(number)-(i+1)].upper())*(base**i)
    count = -1
    for i in range(len(frac[2:])):
        if frac[2:][i].isdigit():
            sumFrac += (int(frac[2:][i])) * (base**count)
            # print(base**count, "base", base, "count", count)
        else:
            print("frac[2:][i])", frac[2:][i])
            print("upper", frac[2:][i].upper())
            sumFrac += hexAlp.get(frac[2:][i].upper()) * (base**count)
            # print(base**count, "base", base, "count", count)
        # print("frac[2:][i]", frac[2:][i])
        # if frac[2:][i] == '1':
        #     sum += base**count
        #     print("sumFrac", sum)
        #     print(base**count, "base", base, "count", count)
        count -= 1
    print("sumFrac", sumFrac)

    print("decoding sum", sum)
    return sum


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    bin = []
    print("type", type(number))
    # frac = ''
    # if digits.isupper() or digits.islower():
    #     number = digits
    # elif isinstance(float(digits), float) == True:
    #     x = float(digits)
    #     frac += str(x-int(x))
    #     number = str(int(float(digits)))
    # print("fraction", frac)

    sub = number
    # Encode number in any base (2 up to 36)
    # else:
    hexAlp = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M',
              23:'N', 24:'O', 25:'P',26: 'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}

    # print("sub is integer", sub.is_integer())
    while sub > 0:
        q, r = divmod(sub, base)
        sub = q
        if r > 9:
            bin.insert(0, hexAlp.get(r).lower())
        else:
            bin.insert(0, r)
    s = ''.join(str(i) for i in bin)
    return s

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    if base1 == 2 and base2 == 16:
        baseTen = decode(digits, base1)
        result = encode(baseTen, base2)
        return result
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    elif base1 == 2 and base2 == 10:
        baseTen = decode(digits, base1)
        result = encode(baseTen, base2)
        return result

    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    elif base1 == 10 and base2 == 16:
        baseTen = decode(digits, base1)
        result = encode(baseTen, base2)
        return result
    # TODO: Convert digits from any base to any base (2 up to 36)
    else:
        baseTen = decode(digits, base1)
        # print("baseTen", baseTen)
        result = encode(baseTen, base2)
        # print("digit", digits, "result", result)
        return result



def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
