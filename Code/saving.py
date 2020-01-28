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
    print("decoding")
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Decode digits from binary (base 2)
    binary = []
    tobebin =[]
    bin = []
    sum = 0
    hexAlp = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20, 'L':21, 'M':22,
              'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}
    # print("decoding")
    if base == 2:
        for i in range(len(digits)):
            if digits[i] == '1':
                sum+=2**((len(digits)-(i+1)))
    #  Decode digits from hexadecimal (base 16) and Decode digits from any base (2 up to 36)
    else:
        # print("decoding starts")
        number = float(digits)
        rounded = str(math.floor(number))
        frac = number - math.floor(number)
        for i in range(len(rounded)):
            # multipying each palce with it's digit place value
            print("digits", digits)
            print("rounded", rounded)
            print(rounded[i])
    #         if digits[len(rounded)-(i+1)].isdigit():
    #             sum += int(rounded[len(rounded)-(i+1)])*(base**i)
    #         else:
    #             sum += hexAlp.get(rounded[len(rounded)-(i+1)].upper())*(base**i)
    #     sum += frac
    # return sum


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
    print("encoding starts number", number)
    number = float(number)
    rounded = math.floor(number)
    sub = rounded
    frac = round(number - math.floor(number), 10)
    s = ''
    # Encode number in binary (base 2)
    if base == 2:
        total = 0
        index = 0
        tobebin =[]
        while sub > 0:
            while total <= sub:
                total = 2**(index)
                index += 1
            total = int(total/2)
            tobebin.append(total)
            sub -= total
            total = 0
            index = 0
        bin = []
        i = 0
        while index != len(tobebin):
            if 2**(i) == tobebin[len(tobebin)-(index+1)]:
                bin.insert(0, 1)
                index += 1
                i+=1
            else:
                bin.insert(0, 0)
                i+=1
        decBin = []
        for i in range(25):
            if 1 > frac > 0:
                frac *= base
                decBin.insert(0, 0)
            elif frac > 1:
                frac = round(frac - math.floor(frac), 10)
                frac *= base
                decBin.insert(1, 1)
        if len(decBin) != 0:
            decBin = decBin[::-1]
            s1 = ''.join(str(item) for item in bin)
            s2 = ''.join(str(item) for item in decBin)
            s = s1+'.'+s2
        return s

    # Encode number in any base (2 up to 36)
    else:
        hexAlp = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M',
                  23:'N', 24:'O', 25:'P',26: 'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}
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
        result = encode(baseTen, base2)
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
