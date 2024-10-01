from random import randint

""" 
Artigo de referencia:
A. Rotenberg. 1960. A New Pseudo-Random Number Generator. J. ACM 7, 1 (Jan. 1960), 75–77. https://doi.org/10.1145/321008.321019

Os parametros 'a', 'c' e 'm' padrões foram retirados do codigo fonte do glibc:
https://sourceware.org/git/?p=glibc.git;a=blob;f=stdlib/random_r.c;hb=glibc-2.26#l362
"""

"""
A classe abaixo implementa o gerador de números pseudo-aleatórios Linear Congruential Generator.
A formula de geração de números é tal que:
    Xn+1 = (a * Xn + c) mod m, onde 'a', 'c' e 'm' são inteiros positivos
De forma a melhorar a qualidade do gerador, a semente inicial deve ser escolhida de forma aleatória
"""
class LinearCongruentialGenerator:
    def __init__(self, a=1103515245, c=12345, m=2**31, seed=None):   
        self._a = a
        self._c = c
        self._m = m
        # garante que uma aleatoria suficientemente válida seja gerada caso não informada
        self._seed = randint(1, m-1) if seed is None else seed
        
    def generate(self) -> int:
        self._seed = (self._a * self._seed + self._c) % self._m
        return self._seed
    
    def generate_n_numbers(self, n : int) -> list:
        return [self.generate() for _ in range(n)]
