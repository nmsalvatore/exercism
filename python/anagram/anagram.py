def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if anagram(word, candidate)]


def anagram(word_1, word_2):
    word_1 = word_1.lower()
    word_2 = word_2.lower()

    return word_1 != word_2 and sorted(word_1) == sorted(word_2)