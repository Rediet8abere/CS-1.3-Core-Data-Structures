import random
import sys

def read_words():
    "Read words file"
    file = open("/usr/share/dict/words")
    # file = open("test.txt")
    content = file.readlines()
    file.close()
    return content

def random_words(word_num=1):
    "Generate sentence constructed by random words"
    words = read_words()
    # print(words)
    # print(word_num)
    random_words = []
    for i in range(int(word_num)):
        random_index = random.randint(0, len(words)-1)
        random_words.append(words[random_index].strip('\n'))
    sentence = ' '.join(random_words)

    # print(sentence)
    return sentence


if __name__ == "__main__":
    params = sys.argv[1:]
    if params:
        word_num = params[0]
        print(random_words(word_num))
    else:
        print("Please pass in a number in the command line. A defualt word is generated.")
        print(random_words())
