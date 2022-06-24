def keep_non_prime_occurrences(A, B):
    # border case
    if len(A) == 0 or len(B) == 0:
        return A

    B_number_quantity, B_max_number = get_number_quantity_and_max(B)
    numbers_to_delete = get_numbers_to_delete(B_number_quantity, B_max_number)

    C = []
    for number in A:
        if number not in numbers_to_delete:
            C.append(number)

    return C


def get_numbers_to_delete(number_quantity, max_number):
    primes_set = sieve_of_eratosthenes(max_number)

    numbers_to_delete = set()
    for number in number_quantity:
        if number_quantity[number] in primes_set:
            numbers_to_delete.add(number)

    return numbers_to_delete


def get_number_quantity_and_max(T):
    number_quantity_map = {}
    max_number = T[0]
    for item in T:
        # update max element
        if item > max_number:
            max_number = item

        # count items quantity
        if item in number_quantity_map:
            current_quantity = number_quantity_map.get(item)
        else:
            current_quantity = 0
        number_quantity_map[item] = current_quantity + 1

    return number_quantity_map, max_number


def sieve_of_eratosthenes(n):
    primes_set = set()
    prime = [True for _ in range(n + 1)]

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            primes_set.add(p)

    return primes_set


if __name__ == '__main__':
    A = [2, 3, 9, 2, 5, 1, 3, 7, 10]
    B = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]
    C = keep_non_prime_occurrences(A, B)
    print(C)
