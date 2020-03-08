
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


def permutations(s):
    # base case
    if len(s) <= 1:
        return [s]
    else:
        perms = []
        #
        for e in permutations(s[:-1]):
            for i in range(len(e)+1):
                perms.append(e[:i] + s[-1] + e[i:])
        return perms


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
    return set_content




def solve_word_jumble(letters, circles, final):
    set_content = read_words()
    letters = [letter.lower() for letter in letters]
    rearrange_list = []
    # to get the word from list of words
    for letter in letters:
        # In this loop word is the rearrangemnt of the word passed
        for word in permutations(letter):
            # O(1) look up for item in set
            # print('set_content', set_content)
            if word in set_content:
                print(word)
                rearrange_list.append(word)
                break
            # else:
            #     print('not found', word)

    letters_wanted = ''
    for i in range(len(circles)):
        for j in range(len(circles[i])):
            # print('circles[i][j]', circles[i][j])
            if circles[i][j] == 'O':
                letters_wanted += rearrange_list[i][j]
    print('letters_wanted', letters_wanted)

    final_arrangemnt = []
    k = 0
    for i in range(len(final)):
        final_arrangemnt.append(letters_wanted[k:len(final[i])+k])
        print(len(final[i]), final_arrangemnt)
        k += len(final[i])
    print('final_arrangemnt', final_arrangemnt)

    return final_arrangemnt

letters = ['LAISA', 'LAURR', 'BUREEK', 'PROUOT']
circles = ['_OOO_', 'O_O__', 'OO____', '__O_OO']
final = ['OOOOO', 'OOOOO']
solve_word_jumble(letters, circles, final)











# def string_permutations(possible_chars, popped=None, possible_comb = [], index = 0):
#     possible_comb = possible_comb
#     string_list = possible_chars
#     print('possible_chars', possible_chars)
#     chars_set = []
#     index = 0
#     for i in range(len(string_list)):
#         # bc a 1
#         popped = possible_chars[index] #c
#         possible_chars.remove(popped) #b
#         # possible_chars = possible_chars[index+1:] #c
#         chars_set.append(popped) #ac
#         # index -= 1
#         print('possible_chars', possible_chars, popped)
#     print('chars_set', chars_set)
#     print('possible_chars', possible_chars)
#     possible_comb.append(chars_set)
#     print('possible_comb', possible_comb)
#     # index += 1
#     print('index', index, string_list)
#     # print(string_list[index+1:], string_list[index])
#     # base case
#     if possible_chars == []:
#         return string_permutations(string_list[index+1:], string_list[index], possible_comb=possible_comb, index=index)
# string_permutations(list('ABC'))
