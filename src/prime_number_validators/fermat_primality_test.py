from src.random_number_generators.linear_congruential import LinearCongruentialGenerator

"""
Verifica se um número é primo utilizando o teste probabilístico de primalidade de Fermat:
- Referencia:
    (material de sala)
- O teste se baseia no pequeno teorema de Fermat, 
- O pequeno teorema de Ferma diz que se 'p' é um número primo e 'a' é um inteiro tal que '1 <= a < p', então 'a^(p-1) ≡ 1 (mod p)'
"""
def fermat_primality(n, n_attemps=20) -> bool:
    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    for _ in range(n_attemps):
        a = LinearCongruentialGenerator().generate(num_bits=n.bit_length(), min=2, max=n-2)
        # a^(n-1) % n
        if pow(a, n - 1, n) != 1:
            return False

    return True
