from src.random_number_generators.linear_congruential import LinearCongruentialGenerator

"""
Verifica se um número é primo utilizando o teste probabilístico de primalidade de Miller-Rabin:
- Referencias: 
    https://inventwithpython.com/rabinMiller.py
    https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
    (material de sala)

- Pseudo-código do teste de primalidade de Miller-Rabin para um número 'n':
    1. Escreva n - 1 = 2^km, onde m é ímpar
    2. Selecione um número aleatório a, 1 < a < n-1
    3. Se a^m mod n = 1
        return True
    4. para i = 0 até k - 1:
        Se a^(2^i)m mod n = n-1
            return True
    5. return False
"""
def miller_rabin(n, n_attempts=20) -> bool:
    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False
    
    # 'm': é impar tal que -> n - 1 = 2^k * m
    # 'k': numero de vezes que 'm' pode ser dividido por 2
    m = n - 1
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    
    for _ in range(n_attempts):
        # 'a': número aleatório tal que 2 <= a <= n - 2
        a = LinearCongruentialGenerator().generate(num_bits=n.bit_length(), min=2, max=n-2)

        # 'ret': a^m % n
        ret = pow(a, m, n)
        # Primeiro teste:
        if ret == 1 or ret == n - 1: # provavelmente primo, continua testando
            continue
        
        # Segundo teste (apenas se falhou no primeiro teste):
        passed = False   
        for _ in range(k - 1):
            ret = pow(ret, 2, n)
            if ret == n - 1:
                passed = True
                break # provavelmente primo, continua testando

        # Falhou nos testes, então 'n' não é primo
        if not passed:
            return False

    # Se passou em todos os testes, então 'n' é provavelmente primo
    return True