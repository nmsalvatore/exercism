def is_triangle(func):
    def inner(sides):
        a, b, c = sorted(sides)
        return a + b >= c and a > 0 and func(sides)
    return inner

@is_triangle
def equilateral(sides):
    return len(set(sides)) < 2

@is_triangle
def isosceles(sides):
    return len(set(sides)) <= 2

@is_triangle
def scalene(sides):
    return len(set(sides)) > 2
