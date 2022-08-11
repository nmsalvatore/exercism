import re

def translate(text):
    words = text.split(' ')
    for index, word in enumerate(words):
        if vowel_sound(word):
            words[index] = word + 'ay'
        elif consonant_sound(word):
            prefix = consonant_sound(word).group()
            words[index] = word.replace(prefix, '') + prefix + 'ay'
    return ' '.join(words)


def vowel_sound(word):
    regex = re.compile(r'^[aeiou]|^xr|^yt')
    result = regex.search(word)
    return result


def consonant_sound(word):
    regex = re.compile(r'^qu|^squ|^y|^[bcdfghjklmnpqrstvwxz]+')
    result = regex.search(word)
    return result
