def append(list1, list2):
    return list1 + list2


def concat(lists):
    return [item for list in lists for item in list]


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return foldl(lambda n, _: n + 1, list, 0)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function, list, initial):
    result = initial
    for item in reverse(list):
        result = function(item, result)
    return result


def reverse(list):
    return list[::-1]
