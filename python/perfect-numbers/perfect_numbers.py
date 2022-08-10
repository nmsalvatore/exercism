def classify(number):
    if number < 1 or type(number) is not int:
        raise ValueError("Classification is only possible for positive integers.")

    factors = [num for num in range(1, number) if number % num == 0]
    aliquot_sum = sum(factors)

    if aliquot_sum == number:
        return 'perfect'
    if aliquot_sum > number:
        return 'abundant'
    if aliquot_sum < number:
        return 'deficient'