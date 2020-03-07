import random

def histogram(content):
    """ Takes a source_text contents of the file as a string and
        return a histogram data structure that stores each unique
        word along with the number of times the word appears in the source text."""
    words = content.split()


    # Dictionary
    histogram_dic = {'one': 1, 'fish': 4}
    print('words', words)
    for index in range(len(words)):
        if not any(words[index] in word_count for word_count in histogram_dic):
            histogram_dic[words[index]] = 1
        else:
            histogram_dic[words[index]] += 1


    return histogram_dic


if __name__ == "__main__":
    file = open("test.txt", "r")
    content = file.read()
    print("histogram in main", histogram(content))
