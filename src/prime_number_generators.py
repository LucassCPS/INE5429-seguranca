from src.random_number_generators.linear_congruential import LinearCongruentialGenerator
from src.random_number_generators.blum_blum_shub import BlumBlumShubGenerator
from src.prime_number_validators import fermat_primality
from src.prime_number_validators import miller_rabin
from enum import Enum

class PrimeGenAlgorithm(Enum):
    LCG = 1
    BBS = 2

class PrimalityCriteria(Enum):
    FERMAT = 1
    MILLER_RABIN = 2
    BOTH = 3

class PrimeNumberGenerator:
    def __init__(self, seed=None):
        self._lcg_generator = LinearCongruentialGenerator(seed=seed)
        self._bbs_generator = BlumBlumShubGenerator(seed=seed)
    
    def _generate_odd_number_LCG(self, num_bits):
        number = self._lcg_generator.generate(num_bits)
        if number % 2 == 0: # Se for par, incrementa 1
            number += 1
        return number
        
    def _generate_odd_number_BBS(self, num_bits):
        number = self._bbs_generator.generate(num_bits)
        if number % 2 == 0: # Se for par, incrementa 1
            number += 1
        return number

    def generate_prime_number_LCG(self, num_bits, n_attempts=20):
        number = self._generate_odd_number_LCG(num_bits)
        while not (fermat_primality(number, n_attempts) and miller_rabin(number, n_attempts)):
            number += 2 
        return number

    
    def generate_prime_number_BBS(self, num_bits, n_attempts=20):
        number = self._generate_odd_number_BBS(num_bits)
        while not fermat_primality(number, n_attempts) and miller_rabin(number, n_attempts):
            number += 2
        return number

    def generate_prime_number_LCG_fermat(self, num_bits, n_attempts=20):
        number = self._generate_odd_number_LCG(num_bits)
        while not fermat_primality(number, n_attempts):
            number += 2
        return number

    def generate_prime_number_BBS_fermat(self, num_bits, n_attempts=20):
        number = self._generate_odd_number_BBS(num_bits)
        while not fermat_primality(number, n_attempts):
            number += 2
        return number

    def generate_prime_number_LCG_miller_rabin(self, num_bits, n_attempts=20):
        number = self._generate_odd_number_LCG(num_bits)
        while not miller_rabin(number, n_attempts):
            number += 2
        return number
    
    def generate_prime_number_BBS_miller_rabin(self, num_bits, n_attempts=20):
        number = self._generate_odd_number_BBS(num_bits)
        while not miller_rabin(number, n_attempts):
            number += 2
        return number