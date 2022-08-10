import re

def is_valid(isbn):
    regex = re.compile(r'(\d)-?(\d{3})-?(\d{5})-?(\d|X)')
    isbn_match = re.fullmatch(regex, isbn)

    try:
        isbn_chars = ''.join(isbn_match.groups())
        return validate(isbn_chars)
    except:
        return False


def validate(isbn):
    result = 0

    for char_index, multiplier in enumerate(range(10,0,-1)):
        char = isbn[char_index]

        if char_index == 9 and char == 'X':
            char = 10

        result += int(char) * multiplier

    return result % 11 == 0