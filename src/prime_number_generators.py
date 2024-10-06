from src.random_number_generators.linear_congruential import LinearCongruentialGenerator
from src.random_number_generators.blum_blum_shub import BlumBlumShubGenerator
from src.prime_number_validators import fermat_primality
from src.prime_number_validators import miller_rabin

# Ao gerar um numero pseudo-aleatório, se ele for par, incrementar/subtrair 1
# Tornar ele o novo numero pseudo-aleatório
# Verificar se ele é primo
class PrimeNumberGenerator:
    def __init__(self):
        pass