from src.random_number_generators import LinearCongruentialGenerator

# adicionar referencias
# usar exponenciação modular

def miller_rabin(n, attemps=10) -> bool:
    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    # continuar...
