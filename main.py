"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    if number <= 0:
        return False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    if number <= 1:
        return []

    prime_factors = []
    factor = 2
    while factor <= int(number**0.5):
        if number % factor == 0 and is_prime(factor):
            count = 0
            while number % factor == 0:
                count += 1
                number //= factor
            prime_factors.extend([factor]*count)
        factor += 1
    if number > 1 and is_prime(number):
        prime_factors.append(number)

    return prime_factors
