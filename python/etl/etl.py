def transform(legacy_data):
    data = {}

    for point, letters in legacy_data.items():
        for letter in letters:
            letter = letter.lower()
            data[letter] = point

    return data