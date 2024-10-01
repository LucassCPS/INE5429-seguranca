from random import randint
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
        # M é o produto de dois primos 'p' e 'q' grandes e congruentes a 3 mod 4
        self._M = p * q
        self._p = p
        self._q = q

        # garante que uma aleatoria suficientemente válida seja gerada caso não informada
        if not seed:
            self._seed = randint(1, self._M - 1)
            # se certifica de que a semente não compartilhe fatores com 'p' ou 'q', ou seja, seja coprima a M (MDC(seed, M) == 1)
            while gcd(self._seed, self._M) != 1:
                self._seed = randint(1, self._M - 1)
        else:
            self._seed = seed
    
    def generate(self) -> int:
        self._seed = (self._seed ** 2) % self._M
        return self._seed
    
    def generate_n_numbers(self, n: int) -> list:
        return [self.generate() for _ in range(n)]
