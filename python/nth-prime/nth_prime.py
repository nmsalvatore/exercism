from math import sqrt


def prime(n):
    if n > 0:
        count, number = 0, 0
        while count < n:
            number += 1
            if is_prime(number):
                count += 1
        return number
    elif n < 0:
        raise ValueError('n must be a value greater than zero')
    else:
        raise ValueError('there is no zeroth prime')


def is_prime(num):
    if num > 1:
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    return False
