from time import time

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

        # Garante que uma aleatoria suficientemente válida seja gerada caso não informada      
        if seed is None:
            curr_time = int(time())
            if curr_time >= 2**31:
                self._seed = curr_time % 2**31
            else:
                self._seed = curr_time
        else:
            self._seed = seed
        
    def generate(self, num_bits=None, min=0, max=None) -> int:
        # Gera um numero pseudo-aleatorio
        self._seed = (self._a * self._seed + self._c) % self._m

        if num_bits is None:
            return self._seed

        # Caso o numero nao tenha o numero de bits desejado, concatena ou trunca ele
        while self._seed.bit_length() != num_bits:
            current_bits = self._seed.bit_length()

            # Se o número de bits for menor que o desejado, concatenamos mais bits
            if current_bits < num_bits:
                append_seed = (self._a * self._seed + self._c) % self._m
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

    def generate_n_numbers(self, n, num_bits=None, min=0, max=None) -> list:
        return [self.generate(num_bits, min, max) for _ in range(n)]
