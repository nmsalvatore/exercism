import re

def count_words(sentence):
    words = get_words(sentence)
    word_counts = dict()
    for word in words:
        if word in word_counts:
            continue
        word_counts[word] = words.count(word)
    return word_counts


def get_words(sentence):
    regex = re.compile(r'[a-zA-Z0-9]+(?:\'[a-z]+)?')
    words = re.findall(regex, sentence)
    words = [word.lower() for word in words]
    return words
