resistors = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
]

def value(colors):
    first = str(resistors.index(colors[0]))
    second = str(resistors.index(colors[1]))
    return int(first + second)