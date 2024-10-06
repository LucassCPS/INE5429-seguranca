from src.prime_number_generators import PrimeNumberGenerator
from time import time

if __name__ == "__main__":
    prime_generator = PrimeNumberGenerator()
    # levando tempo demais para gerar números com 2048 e 4096 bits (dezenas de segundos)
    # quant_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    quant_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024]
    for n_bits in quant_bits:
        begin_t = time()
        prime = prime_generator.generate_prime_number_LCG(num_bits=n_bits)
        end_t = time()
        exec_time = (end_t - begin_t)
        print("Number: ", prime)
        print("Number of bits: ", n_bits)
        print("Generated in: {:.6f} s".format(exec_time))
        print()