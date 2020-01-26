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
    # TODO: Decode digits from binary (base 2)
    # ...
    print("decoding")
    binary = []
    if base == 2:
        # print(digits, base1, base2)
        sum = 0
        for i in range(len(digits)):
            if digits[i] == '1':
                sum+=2**((len(digits)-(i+1)))

        print("sum", sum)
    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    elif base == 16:
        hexAlp = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
        bin = []
        tobebin =[]
        hexa = digits
        for i in range(len(hexa)):
            if hexa[i].isdigit():
                tobebin.append(hexa[i])
            else:
                tobebin.append(hexAlp.get(hexa[i]))
        for i in range(len(tobebin)):
            bin = encode(int(tobebin[i]), 2)
            while len(bin) != 4:
                bin.insert(0, 0)
            binary.extend(bin)
        s = ''.join(str(i) for i in binary)
        decode(s, 2)

    # TODO: Decode digits from any base (2 up to 36)
    # ...


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
    sub = number
    # Encode number in binary (base 2)
    print("base", base)
    if base == 2:
        print("encodeing to base 2")
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

    # Encode number in any base (2 up to 36)
    elif base == 16 or base == 8 or base == 36:
        hexAlp = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M',
                  23:'N', 24:'O', 25:'P',26: 'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}
        while sub > 0:
            q, r = divmod(sub, base)
            sub = q
            if r > 9:
                bin.insert(0, hexAlp.get(r))
            else:
                bin.insert(0, r)
    print("bin", bin)
    return bin
    # s = ''.join(str(i) for i in bin)
    # print("converting", s)

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
    # ...
    # print(len(digits))
    # digitsC = list(digits)
    encode(int(digits), base2)
    print("decoding")
    decode(digits, base1)

    # print(digitsC)
    # for i in range(len(digitsC)):
    #     if len(digitsC) !=8:
    #         digitsC.insert(0,'0')
    #     else:
    #         break
    # print(digits)
    # print("len", len(digitsC))

    # for i in range(len(digits)):
    #     print(digits[len(digits)-(i+1)])
    # if base1 == 2 and base2 == 16:
    #     hexAlp = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    #     hexa = []
    #     total = 0
    #     index = 0
    #     loop = math.ceil((len(digitsC)/4.0))
    #     print("looping",  loop)
    #     for i in range(int(loop)):
    #         count = 0
    #         while count != 4:
    #             print("index", index, "length", len(digitsC)-(index+1), "item", digitsC[len(digitsC)-(index+1)], "count", count)
    #             if (index+1) < len(digitsC):
    #                 if digitsC[len(digitsC)-(index+1)] != '0':
    #                     print("2**count", 2**count)
    #                     total += 2**count
    #                     print("total", total)
    #                 count += 1
    #                 index += 1
    #             else:
    #                 if digitsC[len(digitsC)-(index+1)] != '0':
    #                     print("2**count", 2**count)
    #                     total += 2**count
    #                     print("total", total)
    #                 break
    #         if total <= 9:
    #             hexa.insert(0, total)
    #         elif total in hexAlp.keys():
    #             print("hexAlp.get(total)", hexAlp.get(total))
    #             hexa.append(hexAlp.get(total))
    #         total = 0
    #     print("hexa", hexa)
    # elif base1 == 16 and base2 == 2:
    #     # print("digits", digits)
    #     hexAlp = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    #     bin = []
    #     tobebin =[]
    #     hexa = digits
    #     for i in range(len(hexa)):
    #         if hexa[i].isdigit():
    #             tobebin.append(hexa[i])
    #         else:
    #             tobebin.append(hexAlp.get(hexa[i]))
    #     # print("tobebin", tobebin)
    #     count = 0
    #     bin = []
    #     for i in range(len(tobebin)):
    #         sub = int(tobebin[i])
    #         total = 0
    #         index = 0
    #         inbin = []
    #         # print("tobebin[i]", tobebin[i])
    #         while sub > 0:
    #             while total <= sub:
    #                 total = 2**(index)
    #                 # print("index", index, "total", total, "sub", sub)
    #                 index += 1
    #             total = int(total/2)
    #             sub -= total
    #             # bin.append(total)
    #             inbin.append(total)
    #             # print("total", total, "sub", sub)
    #             # print("inbin", inbin)
    #             index = 0
    #             total = 0
    #         bin.append(inbin)
    #         print("bin", bin)
    #     # bin = [1]
    #     def evaluteing(bin):
    #         binary = []
    #         i = 0
    #         index = 0
    #         count = 0
    #         while index != len(bin):
    #             print("i", i)
    #             if 2**(i) == bin[len(bin)-(index+1)]:
    #                 print("in if", 2**(i), bin[len(bin)-(index+1)])
    #                 print(i, index, bin[len(bin)-(index+1)])
    #                 binary.insert(0, 1)
    #                 index += 1
    #                 i+=1
    #             elif 2**(i) != bin[len(bin)-(index+1)]:
    #                 print("bin", bin)
    #                 print("in else", 2**(i), "i", i, "index", index, "len", len(bin), "bin", bin[len(bin)-(index+1)])
    #                 print(i, index, bin[len(bin)-(index+1)])
    #                 binary.insert(0, 0)
    #                 i+=1
    #                 print("count", count)
    #         return binary
    #
    #     storing = []
    #     for i in range(len(bin)):
    #         print("bbbbbb", bin[i])
    #         storing.append(evaluteing(bin[i]))
    #     print("storing", storing)




        # print("binary", binary)
    #
    #         # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # elif base1 == 2 and base2 == 10:
    #     # print(digits, base1, base2)
    #     sum = 0
    #     for i in range(len(digits)):
    #         if digits[i] == '1':
    #             sum+=2**((len(digits)-(i+1)))
    #
    #     print("sum", sum)
    # elif base1 == 10 and base2 == 2:
    #     pass
        # total = 0
        # index = 0
        # tobebin =[]
        # sub = int(digits)
        # # print("digits", type(int(digits)))
        # while sub > 0:
        #     while total <= sub:
        #         total = 2**(index)
        #         print("index", index, "total", total)
        #         index += 1
        #     total = int(total/2)
        #     print("total", total, "sub", sub)
        #     tobebin.append(total)
        #     sub -= total
        #     print("sub after substraction", sub)
        #     total = 0
        #     index = 0
        #     # break
        # print("tobebin", tobebin, "index", index)
        # print(len(tobebin)-1)
        # bin = []
        # i = 0
        # while index != len(tobebin):
        #     if 2**(i) == tobebin[len(tobebin)-(index+1)]:
        #         print("in if", 2**(i), tobebin[len(tobebin)-(index+1)])
        #         print(i, index, tobebin[len(tobebin)-(index+1)])
        #         bin.insert(0, 1)
        #         index += 1
        #         i+=1
        #     elif 2**(i) != tobebin[len(tobebin)-(index+1)]:
        #         print("in else", 2**(i), tobebin[len(tobebin)-(index+1)])
        #         print(i, index, tobebin[len(tobebin)-(index+1)])
        #         bin.insert(0, 0)
        #         i+=1
        #         # i += 1
        #     elif i == len(tobebin)-1:
        #         print("breaking")
        #         break
        # print("bin", bin)


    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...


    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...



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
