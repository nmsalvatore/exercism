def flatten(iterable):
    result = []

    for item in iterable:
        if item is None:
            continue
        elif type(item) is list:
            result += flatten(item)
        else:
            result.append(item)

    return result