import re

from string import ascii_lowercase
from string import ascii_uppercase

ascii_reverse_lowercase = ascii_lowercase[::-1]


def encode(plain_text):
    standardized_text = standardize(plain_text)
    ENCODE = str.maketrans(ascii_lowercase, ascii_reverse_lowercase)
    encoded_text = standardized_text.translate(ENCODE)
    return encoded_text


def decode(ciphered_text):
    ciphered_text = ''.join(ciphered_text.split(' '))
    DECODE = str.maketrans(ascii_reverse_lowercase, ascii_lowercase)
    decoded_text = ciphered_text.translate(DECODE)
    return decoded_text


def lower(text):
    UPPER_TO_LOWER = str.maketrans(ascii_uppercase, ascii_lowercase)
    lowercase_text = text.translate(UPPER_TO_LOWER)
    return lowercase_text


def standardize(text):
    text = ''.join(re.findall(r'[a-zA-Z0-9]+', text))
    text = ' '.join(re.findall('.{1,5}', text))
    text = lower(text)
    return text
