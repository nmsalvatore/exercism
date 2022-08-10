def sum_of_multiples(limit, multiples):
    unique_multiples = set()

    for num in range(limit):
        for multiple in multiples:
            try:
                if num % multiple == 0:
                    unique_multiples.add(num)
            except:
                continue

    return sum(unique_multiples)