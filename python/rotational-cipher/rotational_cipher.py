from string import ascii_lowercase, ascii_letters

def rotate(text, key):
    key = key % len(ascii_lowercase)
    rotated_lowercase = ascii_lowercase[key:] + ascii_lowercase[:key]
    rotated_letters = rotated_lowercase + rotated_lowercase.upper()
    translation = str.maketrans(ascii_letters, rotated_letters)
    return text.translate(translation)
