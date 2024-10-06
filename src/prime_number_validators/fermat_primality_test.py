from src.random_number_generators.linear_congruential import LinearCongruentialGenerator

# adicionar referencias
# trocar exponenciação built-in por exponenciação modular (olha algoritmo)

"""
Verifica se um número é primo utilizando o teste de primalidade de Fermat
"""
def fermat_primality(n, n_attemps=10) -> bool:
    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    for _ in range(n_attemps):
        a = LinearCongruentialGenerator().generate(n_bits=n.bit_length(), min=0, max=n-1)
        if pow(a, n - 1, n) != 1:
            return False

    return True
