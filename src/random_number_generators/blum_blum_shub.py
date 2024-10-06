from time import time
from math import gcd

"""
Artigo de referência:
L. Blum, M. Blum, and M. Shub, "A Simple Unpredictable Pseudo-Random Number Generator", SIAM Journal on Computing, 1986.
https://people.tamu.edu/~rojas//bbs.pdf
"""

"""
A classe abaixo implementa o gerador de números pseudo-aleatórios Blum Blum Shub.
A formula de geração de números é tal que: 
    Xn+1 = (Xn^2) mod M, sendo M o produto de dois primos 'p' e 'q' grandes e congruentes a 3 mod 4
De forma a melhorar a qualidade do gerador, a semente inicial deve ser escolhida de forma aleatória e ser coprima a M
"""

class BlumBlumShubGenerator:
    def __init__(self, p=1601, q=2027, seed=None):
        self._M = p * q
        self._p = p
        self._q = q

        # Garante que uma aleatoria suficientemente válida seja gerada caso não informada
        if seed is None:
            self._seed = int(time())
            # Certifica-se de que a semente não compartilhe fatores com 'p' ou 'q', ou seja, seja coprima a M (MDC(seed, M) == 1)
            while gcd(self._seed, self._M) != 1:
                self._seed = int(time())
        else:
            self._seed = seed
    
    def generate(self, num_bits, min=0, max=None) -> int:
        # Gera um numero pseudo-aleatorio
        self._seed = (self._seed ** 2) % self._M

        # Caso o numero nao tenha o numero de bits desejado, concatena ou trunca ele
        while self._seed.bit_length() != num_bits:
            current_bits = self._seed.bit_length()

            # Se o número de bits for menor que o desejado, concatenamos mais bits
            if current_bits < num_bits:
                append_seed = (self._seed ** 2) % self._M
                append_seed_bits = append_seed.bit_length()

                # Calcula quantos bits ainda faltam
                bits_needed = num_bits - current_bits

                # Se o número de bits do numero a ser apendado for maior que o necessário, trunca ele
                if append_seed_bits > bits_needed:
                    append_seed = append_seed >> (append_seed_bits - bits_needed)
                
                # Realiza a concatenação
                self._seed = (self._seed << bits_needed) | append_seed

            # Caso o número de bits seja maior do que o desejado, removemos os bits excedentes à direita
            elif current_bits > num_bits:
                self._seed = self._seed >> (current_bits - num_bits)

        # Certifica-se de que o número gerado esteja entre min e max
        if max is not None:
            self._seed = (self._seed % (max - min)) + min
        else:
            self._seed += min

        return self._seed    

    def generate_n_numbers(self, n, num_bits, min=0, max=None) -> list:
        return [self.generate(num_bits, min, max) for _ in range(n)]
