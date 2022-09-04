LINES = (
    ('first', 'a Partridge in a Pear Tree.'),
    ('second', 'two Turtle Doves, '),
    ('third', 'three French Hens, '),
    ('fourth', 'four Calling Birds, '),
    ('fifth', 'five Gold Rings, '),
    ('sixth', 'six Geese-a-Laying, '),
    ('seventh', 'seven Swans-a-Swimming, '),
    ('eighth', 'eight Maids-a-Milking, '),
    ('ninth', 'nine Ladies Dancing, '),
    ('tenth', 'ten Lords-a-Leaping, '),
    ('eleventh', 'eleven Pipers Piping, '),
    ('twelfth', 'twelve Drummers Drumming, ')
)

def recite(start_verse, end_verse):
    result = []

    for verse_index in range(start_verse-1, end_verse):
        day_num = LINES[verse_index][0]
        verse = f'On the {day_num} day of Christmas my true love gave to me: '

        for line_index in range(verse_index, -1, -1):
            gift = LINES[line_index][1]
            if line_index == 0 and verse_index != 0:
                verse += 'and ' + gift
            else:
                verse += gift

        result.append(verse)

    return result
