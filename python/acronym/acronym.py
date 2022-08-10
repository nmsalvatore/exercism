import re

def abbreviate(str):
    words = re.compile(r'[a-zA-Z\']+').findall(str)
    acronym = ''.join([word[0].upper() for word in words])
    return acronym
