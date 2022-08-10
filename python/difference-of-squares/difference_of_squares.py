def square_of_sum(number):
    return sum(n+1 for n in range(number))**2


def sum_of_squares(number):
    return sum((n+1)**2 for n in range(number))


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
