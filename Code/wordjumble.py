
# word = ['r', 'e', 'd', 'i']
# rearrange = []
# count = 0
# while count < 13:
#     for j in range(len(word)):
#         if j+1 < len(word):
#             temp = word[j]
#             word[j] = word[j+1]
#             word[j+1] = temp
#             print('word', word)
#             rearrange.append(''.join(word))
#             count += 1
#             # print(''.join(word))
# print('rearrange', rearrange, len(rearrange))
import search


def read_words():
    "Read words file"
    file = open("/usr/share/dict/words")

    # instantiate a set object
    set_content = set()
    while True:
        # get word from file
        word = file.readline().strip()
        if not word:
            break
        # keep adding word to the set
        set_content.add(word)

    # print(set_content)
    if 'God' in set_content:
        print('God')

    # loop through the list of words in content
    # to find the ordSum for each word
    # ordSum_words = {}
    # for word in content:
    #     # print(word)
    #     ordSum = sum(ord(letter) for letter in word.strip())
        # print('ordSum', ordSum)

        # a dictonary to hold the ascii sum of a word as a key
        # and all the words with the same ascii sum in a set as a value

        # we check if the ordSum exists as a key
        # words = ordSum_words.get(ordSum, None)
        # if words != None:
        #     # print('word')
        #     # if so we add a word in a set that has the same ordSum
        #     words.add(word.strip())
        # else:
        #     # print(words_set)
        #     ordSum_words[ordSum] = set(word.strip())

    # print(ordSum_words)
    # print('dictionary')
    #
    # file.close()
    # return content

dictionary_words = read_words()
#
# def calculate_asciiValue(word):
#     asciiValue = 0
#     for letter in word:
#         asciiValue += ord(letter)
#     print('asciiValue', asciiValue)
#
# calculate_asciiValue('redi')





# print('words_rearranged', words_rearranged)
# logical_word = []
# for word in words_rearranged:
# s = 'A'
# for dict_word in dictionary_words:
#     print(dict_word)
#     print(dict_word, s, dict_word == s)
#     print(ord(s))
#     print(ord(dict_word))
#
#     break
        # if word == dict_word:
    # print(word)
    # print(word)
    # break
    # print(search.binary_search(dictionary_words, word))
    # if search.binary_search(dictionary_words, word) != None:
    #     logical_word.append(word)
# print('logical_word', logical_word)
