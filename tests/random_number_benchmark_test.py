from src.random_number_generators.linear_congruential import LinearCongruentialGenerator
from src.random_number_generators.blum_blum_shub import BlumBlumShubGenerator
from time import time

# Lista de bits a serem utilizados na geração de números
quant_bits_list = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
report_file = "tests/reports/random_number_generation_report.txt"

def generate_random_numbers(generator, num_bits, n=100000):
    times = []
    for _ in range(n):
        start_time = time()
        generator.generate(num_bits=num_bits)
        times.append((time() - start_time) * 1000)
    return times

def calculate_average(times):
    return sum(times) / len(times)

def generate_report(file_path=report_file):
    lcg_generator = LinearCongruentialGenerator()
    bbs_generator = BlumBlumShubGenerator()

    with open(file_path, "w") as file:
        file.write("Random Number Generation Report\n")
        file.write("-" * 60 + "\n")

        for bits in quant_bits_list:
            # Geração LCG
            lcg_times = generate_random_numbers(lcg_generator, bits)
            lcg_avg_time = calculate_average(lcg_times)
            file.write(f"LCG - {bits} bits - Avg Time: {lcg_avg_time:.10} ms\n")
            
            # Geração BBS
            bbs_times = generate_random_numbers(bbs_generator, bits)
            bbs_avg_time = calculate_average(bbs_times)
            file.write(f"BBS - {bits} bits - Avg Time: {bbs_avg_time:.10} ms\n")
            
            file.write("-" * 60 + "\n")
