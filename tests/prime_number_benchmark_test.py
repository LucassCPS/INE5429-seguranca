from src.prime_number_generators import PrimeNumberGenerator, PrimeGenAlgorithm, PrimalityCriteria
from time import time
from subprocess import Popen, PIPE

# Lista de bits a serem utilizados na geração de primos
quant_bits_list = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
prime_generator = PrimeNumberGenerator()
report_file = "tests/reports/prime_number_generation_report.txt"

def generate_prime_number(algorithm: PrimeGenAlgorithm, primality_criteria: PrimalityCriteria, bits: int):
    if algorithm == PrimeGenAlgorithm.LCG and primality_criteria == PrimalityCriteria.FERMAT:
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

def generate_prime_numbers_and_times(algorithm: PrimeGenAlgorithm, primality_criteria: PrimalityCriteria, bits: int, num_samples: int = 50):
    times = []
    if bits == 2048 or bits == 4096:
        num_samples = 10
    for _ in range(num_samples):
        start_time = time()
        prime = generate_prime_number(algorithm, primality_criteria, bits)
        exec_time = (time() - start_time)
        times.append(exec_time)
    return times

def calculate_average(times):
    return sum(times) / len(times)

def generate_prime_number_report(algorithm: PrimeGenAlgorithm, primality_criteria: PrimalityCriteria, file_path):
    with open(file_path, "a") as file:
        for bits in quant_bits_list:
            times = generate_prime_numbers_and_times(algorithm, primality_criteria, bits)
            avg_time = calculate_average(times)
            file.write(f"{algorithm.name} - {primality_criteria.name} - {bits} bits - Avg Time: {avg_time:.7f} s\n")

def generate_report(file_path=report_file):
    with open(file_path, "w") as file:
        file.write("Prime Number Generation Report\n")
        file.write("-" * 60 + "\n")

    combinations = [(PrimeGenAlgorithm.LCG, PrimalityCriteria.FERMAT),
                    (PrimeGenAlgorithm.LCG, PrimalityCriteria.MILLER_RABIN)]

    for algorithm, criteria in combinations:
        header = f"{algorithm.name} - {criteria.name}\n"
        with open(file_path, "a") as file:
            file.write(header)
        generate_prime_number_report(algorithm, criteria, file_path)
        with open(file_path, "a") as file:
            file.write("-" * 60 + "\n")
