VERSES = {
    1: ('that lay in', 'the house that Jack built.'),
    2: ('that ate', 'the malt'),
    3: ('that killed', 'the rat'),
    4: ('that worried ', 'the cat '),
    5: ('that tossed ', 'the dog '),
    6: ('that milked ', 'the cow with the crumpled horn '),
    7: ('that kissed ', 'the maiden all forlorn '),
    8: ('that married ', 'the man all tattered and torn '),
    9: ('that woke ', 'the priest all shaven and shorn '),
    10: ('that kept ', 'the rooster that crowed in the morn '),
    11: ('that belonged to ', 'the farmer sowing his corn '),
    12: (None, 'the horse and the hound and the horn '),
}

def get_verse(verse_num):
    verse = ''
    for num in range(verse_num, 0, -1):
        if num == verse_num:
            verse += f'This is {VERSES.get(verse_num)[1]}'
        else:
            verse += f'{VERSES.get(num)[0]} {VERSES.get(num)[1]}'
    
    return verse

def recite(start_verse, end_verse):
    verses = []
    for verse_num in range(start_verse, end_verse+1):
        verse = get_verse(verse_num)
        verses.append(verse)
    
    return verses

print( get_verse(3) )

