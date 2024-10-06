from src.random_number_generators.linear_congruential import LinearCongruentialGenerator
from src.random_number_generators.blum_blum_shub import BlumBlumShubGenerator
from src.prime_number_validators import fermat_primality
from src.prime_number_validators import miller_rabin
from src.prime_number_generators import PrimeNumberGenerator

def generate_numbers_LCG(n_random_numbers, num_bits, new_seed=None) -> list:
    generator = LinearCongruentialGenerator(seed=new_seed)
    random_numbers_list = generator.generate_n_numbers(n_random_numbers, num_bits)
    
    return random_numbers_list

def generate_numbers_BBS(n_random_numbers, num_bits, new_seed=None) -> list:
    generator = BlumBlumShubGenerator(seed=new_seed)
    random_numbers_list = generator.generate_n_numbers(n_random_numbers, num_bits)
    
    return random_numbers_list

if __name__ == "__main__":
    print(generate_numbers_LCG(n_random_numbers=1, num_bits=128))
    print(generate_numbers_BBS(n_random_numbers=1, num_bits=128))
