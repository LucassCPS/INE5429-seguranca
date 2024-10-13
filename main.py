from src.prime_number_generators import PrimeNumberGenerator, PrimeGenAlgorithm, PrimalityCriteria
from time import time
from subprocess import Popen, PIPE

# Lista de bits a serem utilizados na geração de primos
quant_bits_list = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
prime_generator = PrimeNumberGenerator()

def generate_prime_number(algorithm: PrimeGenAlgorithm, primality_criteria: PrimalityCriteria, bits: int):
    if algorithm == PrimeGenAlgorithm.LCG and primality_criteria == PrimalityCriteria.BOTH:
        return prime_generator.generate_prime_number_LCG(num_bits=bits)
    elif algorithm == PrimeGenAlgorithm.BBS and primality_criteria == PrimalityCriteria.BOTH:
        return prime_generator.generate_prime_number_BBS(num_bits=bits)
    elif algorithm == PrimeGenAlgorithm.LCG and primality_criteria == PrimalityCriteria.FERMAT:
        return prime_generator.generate_prime_number_LCG_fermat(num_bits=bits)
    elif algorithm == PrimeGenAlgorithm.BBS and primality_criteria == PrimalityCriteria.FERMAT:
        return prime_generator.generate_prime_number_BBS_fermat(num_bits=bits)
    elif algorithm == PrimeGenAlgorithm.LCG and primality_criteria == PrimalityCriteria.MILLER_RABIN:
        return prime_generator.generate_prime_number_LCG_miller_rabin(num_bits=bits)
    elif algorithm == PrimeGenAlgorithm.BBS and primality_criteria == PrimalityCriteria.MILLER_RABIN:
        return prime_generator.generate_prime_number_BBS_miller_rabin(num_bits=bits)

def openssl_prime_check(prime: int):
    cmd = f"openssl prime {prime}"
    result = Popen(cmd, stdout=PIPE, shell=True).stdout.read().decode('utf-8')

    if "not" in result:
        return "not a prime"
    return "prime"

def generate_prime_number_report(algorithm: PrimeGenAlgorithm, primality_criteria: PrimalityCriteria, report_file):
    with open(report_file, "a") as file:
        for bits in quant_bits_list:
            begin_t = time()
            prime = generate_prime_number(algorithm, primality_criteria, bits)
            exec_time = time() - begin_t
            openssl_result = openssl_prime_check(prime)

            report = (f"Number: {prime}\n"
                      f"Number of bits: {bits}\n"
                      f"Generated in:  {exec_time:.10f}s\n"
                      f"Openssl test evaluation: {openssl_result}\n\n")

            file.write(report)

if __name__ == "__main__":
    report_file = "prime_number_report.txt"

    with open(report_file, "w") as file:
        file.write("Prime Number Generation Report\n")
        file.write("-" * 60 + "\n")

    combinations = [
        (PrimeGenAlgorithm.LCG, PrimalityCriteria.FERMAT),
        (PrimeGenAlgorithm.BBS, PrimalityCriteria.FERMAT),
        (PrimeGenAlgorithm.LCG, PrimalityCriteria.MILLER_RABIN),
        (PrimeGenAlgorithm.BBS, PrimalityCriteria.MILLER_RABIN)
    ]

    for algorithm, criteria in combinations:
        header = f"{algorithm.name} - {criteria.name}\n"
        with open(report_file, "a") as file:
            file.write(header)
        generate_prime_number_report(algorithm, criteria, report_file)
        with open(report_file, "a") as file:
            file.write("-" * 60 + "\n")
